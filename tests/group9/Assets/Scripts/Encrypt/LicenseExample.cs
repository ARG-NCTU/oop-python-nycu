using UnityEngine;

namespace DeviceLicensing.Example
{
    /// <summary>
    /// 使用範例 - 展示如何在遊戲中使用設備授權系統
    /// Usage Example - Shows how to use device licensing system in games
    /// </summary>
    public class LicenseExample : MonoBehaviour
    {
        private void Start()
        {
            // 確保 DeviceLicenseManager 存在
            // Make sure DeviceLicenseManager exists
            if (DeviceLicenseManager.Instance == null)
            {
                // 創建 DeviceLicenseManager
                GameObject licenseManagerObj = new GameObject("DeviceLicenseManager");
                licenseManagerObj.AddComponent<DeviceLicenseManager>();
            }
            
            // 訂閱授權狀態變更事件
            // Subscribe to license status change event
            DeviceLicenseManager.Instance.OnLicenseStatusChanged += OnLicenseStatusChanged;
            
            // 檢查授權狀態
            // Check license status
            if (DeviceLicenseManager.Instance.IsLicensed)
            {
                Debug.Log("應用已授權，可以正常使用。");
                Debug.Log("Application is licensed, ready to use.");
                StartGame();
            }
            else
            {
                Debug.Log($"應用未授權。設備碼: {DeviceLicenseManager.Instance.DeviceCode}");
                Debug.Log($"Application is not licensed. Device Code: {DeviceLicenseManager.Instance.DeviceCode}");
                ShowLicenseUI();
            }
        }
        
        private void OnDestroy()
        {
            if (DeviceLicenseManager.Instance != null)
            {
                DeviceLicenseManager.Instance.OnLicenseStatusChanged -= OnLicenseStatusChanged;
            }
        }
        
        private void OnLicenseStatusChanged(bool isLicensed)
        {
            if (isLicensed)
            {
                Debug.Log("授權成功！");
                Debug.Log("License activated!");
                StartGame();
            }
            else
            {
                Debug.Log("授權已失效。");
                Debug.Log("License deactivated.");
                ShowLicenseUI();
            }
        }
        
        private void StartGame()
        {
            // 在這裡開始您的遊戲邏輯
            // Start your game logic here
            Debug.Log("遊戲開始！");
            Debug.Log("Game started!");
        }
        
        private void ShowLicenseUI()
        {
            // 在這裡顯示授權UI
            // Show license UI here
            Debug.Log("請輸入授權密碼以繼續。");
            Debug.Log("Please enter license password to continue.");
        }
        
        // 測試用：在 Inspector 中可以調用此方法來測試授權
        // For testing: Can call this method from Inspector to test licensing
        [ContextMenu("Test License with Sample Code")]
        public void TestLicenseValidation()
        {
            string deviceCode = DeviceLicenseManager.Instance.DeviceCode;
            Debug.Log($"當前設備碼 / Current Device Code: {deviceCode}");
            Debug.Log("請使用 LicenseGenerator 工具生成密碼。");
            Debug.Log("Please use LicenseGenerator tool to generate password.");
        }
    }
}
