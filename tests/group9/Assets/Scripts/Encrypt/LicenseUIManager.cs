using UnityEngine;
using UnityEngine.UI;

namespace DeviceLicensing
{
    /// <summary>
    /// 授權UI管理器 - 提供授權介面
    /// License UI Manager - Provides license interface
    /// </summary>
    public class LicenseUIManager : MonoBehaviour
    {
        [Header("UI References")]
        [SerializeField] private GameObject licensePanel;
        [SerializeField] private Text deviceCodeText;
        [SerializeField] private InputField passwordInput;
        [SerializeField] private Button activateButton;
        [SerializeField] private Button copyDeviceCodeButton;
        [SerializeField] private Text statusText;
        
        [Header("Settings")]
        [SerializeField] private bool showOnStart = true;
        [SerializeField] private bool hideOnSuccess = true;
        
        private DeviceLicenseManager _licenseManager;
        
        private void Start()
        {
            _licenseManager = DeviceLicenseManager.Instance;
            
            if (_licenseManager == null)
            {
                Debug.LogError("[LicenseUI] DeviceLicenseManager not found! Please add it to the scene.");
                return;
            }
            
            // 設置UI
            SetupUI();
            
            // 訂閱事件
            _licenseManager.OnLicenseStatusChanged += OnLicenseStatusChanged;
            
            // 初始顯示
            if (showOnStart && !_licenseManager.IsLicensed)
            {
                ShowLicensePanel();
            }
            else if (_licenseManager.IsLicensed)
            {
                HideLicensePanel();
            }
        }
        
        private void OnDestroy()
        {
            if (_licenseManager != null)
            {
                _licenseManager.OnLicenseStatusChanged -= OnLicenseStatusChanged;
            }
        }
        
        private void SetupUI()
        {
            // 顯示設備碼
            if (deviceCodeText != null)
            {
                deviceCodeText.text = _licenseManager.DeviceCode;
            }
            
            // 設置按鈕事件
            if (activateButton != null)
            {
                activateButton.onClick.AddListener(OnActivateButtonClicked);
            }
            
            if (copyDeviceCodeButton != null)
            {
                copyDeviceCodeButton.onClick.AddListener(OnCopyDeviceCodeClicked);
            }
            
            UpdateStatusText();
        }
        
        private void OnActivateButtonClicked()
        {
            if (passwordInput == null) return;
            
            string password = passwordInput.text;
            bool success = _licenseManager.ValidateLicense(password);
            
            if (success)
            {
                UpdateStatusText("授權成功！License activated!");
                if (hideOnSuccess)
                {
                    HideLicensePanel();
                }
            }
            else
            {
                UpdateStatusText("授權失敗，請檢查密碼。License failed, please check password.");
            }
        }
        
        private void OnCopyDeviceCodeClicked()
        {
            GUIUtility.systemCopyBuffer = _licenseManager.DeviceCode;
            UpdateStatusText("設備碼已複製到剪貼板！Device code copied!");
        }
        
        private void OnLicenseStatusChanged(bool isLicensed)
        {
            UpdateStatusText();
            
            if (isLicensed && hideOnSuccess)
            {
                HideLicensePanel();
            }
        }
        
        private void UpdateStatusText(string message = null)
        {
            if (statusText == null) return;
            
            if (!string.IsNullOrEmpty(message))
            {
                statusText.text = message;
            }
            else
            {
                statusText.text = _licenseManager.IsLicensed ? 
                    "已授權 Licensed" : 
                    "未授權 Not Licensed";
            }
        }
        
        public void ShowLicensePanel()
        {
            if (licensePanel != null)
            {
                licensePanel.SetActive(true);
            }
        }
        
        public void HideLicensePanel()
        {
            if (licensePanel != null)
            {
                licensePanel.SetActive(false);
            }
        }
    }
}
