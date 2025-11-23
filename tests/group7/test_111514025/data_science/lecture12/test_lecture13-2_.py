import random
import numpy as np
import cluster

class Patient(cluster.Example):
    pass

def scaleAttrs(vals):
    vals = np.array(vals, dtype=float)
    mean = np.mean(vals)
    sd = np.std(vals)
    if sd == 0:
        return vals - mean  # 避免除以 0
    return (vals - mean) / sd

def getData(toScale=False):
    points = []
    try:
        with open('tests/group7/test_111514025/data_science/lecture12/cardiacData.txt', 'r') as f:
            for i, line in enumerate(f):
                if line.strip() == '':
                    continue
                vals = line.strip().split(',')
                if len(vals) != 5:
                    continue
                hr = int(vals[0])
                st_elev = int(vals[1])
                age = int(vals[2])
                prev_acs = int(vals[3])
                label = int(vals[4])
                
                features = np.array([hr, prev_acs, st_elev, age], dtype=float)
                if toScale:
                    # 這裡不做整體 scale，題目通常不要求
                    pass
                patient = Patient('P' + str(i), features, label)
                points.append(patient)
    except FileNotFoundError:
        print("錯誤：找不到 cardiacData.txt")
        print("請確認 cardiacData.txt 放在以下目錄：")
        import os
        print(os.getcwd())
        print("目前資料夾內檔案：", os.listdir('.'))
        exit()
    
    print(f"成功載入 {len(points)} 位病患資料")
    return points

def kmeans(examples, k, verbose=False):
    if k <= 0 or k > len(examples):
        raise ValueError('k 不合法')
    
    # 隨機選 k 個初始中心
    initial = random.sample(examples, k)
    clusters = [cluster.Cluster([ex]) for ex in initial]
    
    iteration = 0
    converged = False
    while not converged:
        iteration += 1
        new_assignments = [[] for _ in range(k)]
        
        # 分配每個點到最近的中心
        for ex in examples:
            distances = [ex.distance(clusters[i].getCentroid()) for i in range(k)]
            closest = distances.index(min(distances))
            new_assignments[closest].append(ex)
        
        # 檢查是否有空群集
        if any(len(assignment) == 0 for assignment in new_assignments):
            raise ValueError("出現空群集")
        
        # 更新群集
        converged = True
        for i in range(k):
            moved = clusters[i].update(new_assignments[i])
            if moved > 0:
                converged = False
        
        if verbose:
            print(f"\nIteration {iteration}")
            for c in clusters:
                print(c)
    
    return clusters

def trykmeans(examples, numClusters, numTrials, verbose=False):
    best = None
    best_diss = float('inf')
    
    for trial in range(numTrials):
        if verbose:
            print(f"\n=== 第 {trial+1}/{numTrials} 次嘗試 ===")
        try:
            clusters = kmeans(examples, numClusters, verbose)
            diss = cluster.dissimilarity(clusters)
            if diss < best_diss:
                best_diss = diss
                best = clusters
                if verbose:
                    print(f"找到更優解！不相似度 = {diss:.4f}")
        except ValueError:
            if verbose:
                print("此次初始化產生空群集，跳過")
            continue
    
    if best is None:
        raise RuntimeError("所有嘗試都失敗")
    return best

def printClustering(clustering):
    posFracs = []
    for i, c in enumerate(clustering):
        points = c.getPoints()
        numPos = sum(1 for p in points if p.getLabel() == 1)
        frac = numPos / len(points) if points else 0
        posFracs.append(frac)
        print(f"Cluster {i+1}: {len(points)} 人，其中陽性比例 = {frac:.4f}")
    return np.array(posFracs)

# ===================== 主程式 =====================
if __name__ == "__main__":
    patients = getData(toScale=False)
    
    print("\n" + "="*60)
    print("開始執行 k-means 分群 (k=2)")
    print("="*60)
    
    random.seed(2)  # 題目要求
    best_clustering = trykmeans(patients, numClusters=2, numTrials=20, verbose=False)
    
    printClustering(best_clustering)
    
    # 總陽性病患數（可選）
    total_pos = sum(1 for p in patients if p.getLabel() == 1)
    print(f"\n總陽性病患數 = {total_pos}")