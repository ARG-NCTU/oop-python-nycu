def test_lab16():
    import pandas as pd
    import geopandas as gpd
    from geopandas import GeoDataFrame, read_file
    from shapely.geometry import Point, LineString
    import numpy as np

    import sys
    sys.path.append("..")
    import movingpandas as mpd
    # mpd.show_versions()

    from datetime import datetime

    import warnings
    warnings.simplefilter("ignore")
    import matplotlib.pyplot as plt

    boats = ['wamv1', 'wamv2', 'wamv3', 'wamv4', 'wamv5']
    wamvs = {}
    trajs = {}
    
    import os
    this_dir = os.path.dirname(__file__)
    for boat in boats:
        csv_path = os.path.join(this_dir, 'data', 'bory_boat', boat + '_gps.csv')

        # 讀取 CSV
        df = pd.read_csv(csv_path, delimiter=',')
        #csv_path = os.path.join(this_dir, 'sales_data.csv')
        #df = pd.read_csv(csv_path)
        #df = pd.read_csv('data/bory_boat/' + boat + '_gps.csv', delimiter=',')
        df['t'] = pd.to_datetime(df['t'], unit='ns')
        wamv = df[['X', 'Y', 'trajectory_id', 't']]
        wamv['geometry'] = df.apply(lambda row: Point(row['X'], row['Y']), axis=1)

        gdf = gpd.GeoDataFrame(wamv, geometry='geometry', crs='EPSG:4326')
        gdf = gdf.to_crs(epsg=32649) # Convert to UTM zone 49N for Taiwan

        trajs[boat] = mpd.Trajectory(gdf, 'trajectory_id', t='t')
        wamvs[boat] = gdf

    wamvs['wamv1']
    merged_gdf = pd.concat([wamvs['wamv1'], wamvs['wamv2'], wamvs['wamv3'], wamvs['wamv4'], wamvs['wamv5']], axis=0)
    merged_gdf
    traj_collection = mpd.TrajectoryCollection(merged_gdf, 'trajectory_id', t='t')
    traj_collection.add_speed()
    traj_collection.get_max('speed')
    traj_collection.plot(column='speed', legend=True, figsize=(9,5))
    traj_collection.add_direction()
    traj_collection.plot(column='direction', legend=True, figsize=(9,5))
    traj_collection.get_start_locations()

    traj_collection.get_end_locations()
    t1 = datetime(1970,1,1,0,14,14)
    t2 = datetime(1970,1,1,0,15,44)
    traj_collection.get_segments_between(t1, t2).plot(column='speed', legend=True, figsize=(9,5))
    #Demo 1 
    summary = []
    for traj in traj_collection.trajectories:
        
        length = traj.get_length()
        duration = traj.get_duration().total_seconds()  # Duration in second
        avg_speed = length / duration if duration > 0 else 0  # Avoid division by zero  

        #############  code below  #############
        # Hint: avg_speed = length / duration

        #############  code above  #############
        summary.append({
            "trajectory_id": traj.id,
            "total_distance(m)": length,
            "avg_speed(m/s)": avg_speed,
        })

    summary_df = pd.DataFrame(summary)
    print(summary_df)
    # Demo 2
    import geopandas as gpd

    fig, ax = plt.subplots(figsize=(10, 8))

    low_speed_points_list = []

    for traj in traj_collection.trajectories:
        traj.plot(ax=ax, linewidth=2, alpha=0.7, label=traj.id)
        
        # #############  code below  #############
        # 取得速度小於 0.1 m/s 的點
        low_speed_points = traj.df[traj.df["speed"] < 0.1]
        
        # 直接使用 geometry 欄位轉成 GeoSeries
        low_speed_gs = gpd.GeoSeries(low_speed_points["geometry"], crs=traj.df.crs)  # 或者 crs="EPSG:4326"
        
        # 收集到列表
        low_speed_points_list.append(low_speed_gs)
        
        # 畫出低速點
        low_speed_gs.plot(ax=ax, color="red", markersize=20, label=f"({traj.id})")
        # #############  code above  #############

    ax.legend()
    plt.title("Trajectory with low-speed points (speed < 0.1 m/s)")
    plt.show()
    # Demo 3
    directions = traj.df["direction"]

    print(directions.describe())

    import numpy as np
    import geopandas as gpd
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 8))

    turning_points = {}
    TURN_ANGLE_THRESHOLD = 45  # degrees
    MOVE_DISTANCE_THRESHOLD = 2  # meters
    LOOKAHEAD = 5  # 往後看的點數

    for traj in traj_collection.trajectories:
        
        df = traj.df.reset_index(drop=True)
        directions = df["direction"]

        turning_indices = []

        for i in range(len(df)):
            direction_A = directions[i]
            point_A = df.iloc[i].geometry
            
            # for j in range(1, LOOKAHEAD + 1):
            index_B = i + LOOKAHEAD
            if index_B >= len(directions):
                continue

            direction_B = directions[index_B]
            point_B = df.iloc[index_B].geometry

            # 計算方向差（處理循環問題）
            angle_diff = abs(direction_A - direction_B) % 360
            if angle_diff > 180:
                angle_diff = 360 - angle_diff

            # 計算距離
            #print(distance)
            distance = point_A.distance(point_B)

            if angle_diff > TURN_ANGLE_THRESHOLD and distance < MOVE_DISTANCE_THRESHOLD:
                turning_indices.append(i)
            

        turning_points_gs = gpd.GeoSeries(df.loc[turning_indices, "geometry"], crs=traj.df.crs)
        turning_points[traj.id] = turning_points_gs
        print(f"Trajectory {traj.id} has {len(turning_points_gs)} turning points.")

        traj.plot(ax=ax, linewidth=2, alpha=0.7, label=traj.id)
        turning_points_gs.plot(ax=ax, color="red", markersize=30, label=f"Turning ({traj.id})")

    ax.legend()
    plt.title('Turning Points: |ΔDirection| > 45°, Distance < 2m (within next 5 points)')
    plt.xlabel("Easting (m)")
    plt.ylabel("Northing (m)")
    plt.show()

