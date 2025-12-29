using System;
using System.Security.Cryptography;
using System.Text;
using UnityEngine;

namespace DeviceLicensing
{
    /// <summary>
    /// 設備授權管理器 - 用於在 Unity 中驗證設備授權
    /// Device License Manager - For validating device licenses in Unity
    /// </summary>
    public class DeviceLicenseManager : MonoBehaviour
    {
        private const string LICENSE_KEY = "DeviceLicense_Key";
        private const string SECRET_SALT = "Unity_Device_License_Salt_2024";
        
        private static DeviceLicenseManager _instance;
        public static DeviceLicenseManager Instance => _instance;
        
        /// <summary>
        /// 授權狀態變更事件
        /// License status change event
        /// </summary>
        public event Action<bool> OnLicenseStatusChanged;
        
        /// <summary>
        /// 當前是否已授權
        /// Whether currently licensed
        /// </summary>
        public bool IsLicensed { get; private set; }
        
        /// <summary>
        /// 設備碼 (用戶需要發送給開發者的碼)
        /// Device code (code that user needs to send to developer)
        /// </summary>
        public string DeviceCode { get; private set; }
        
        private void Awake()
        {
            if (_instance != null && _instance != this)
            {
                Destroy(gameObject);
                return;
            }
            
            _instance = this;
            DontDestroyOnLoad(gameObject);
            
            // 生成設備碼
            DeviceCode = GenerateDeviceCode();
            
            // 檢查已保存的授權
            CheckSavedLicense();
        }
        
        /// <summary>
        /// 獲取設備的唯一標識符
        /// Get the unique identifier of the device
        /// </summary>
        private string GetDeviceIdentifier()
        {
            // 使用 Unity 的 deviceUniqueIdentifier
            // 這在每台設備上是唯一的
            return SystemInfo.deviceUniqueIdentifier;
        }
        
        /// <summary>
        /// 根據設備標識符生成固定的設備碼
        /// Generate a fixed device code based on device identifier
        /// </summary>
        private string GenerateDeviceCode()
        {
            string deviceId = GetDeviceIdentifier();
            
            // 使用 SHA256 生成固定的哈希值
            using (SHA256 sha256 = SHA256.Create())
            {
                string combined = deviceId + SECRET_SALT;
                byte[] hashBytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(combined));
                
                // 轉換為大寫的十六進制字符串，取前16個字符作為設備碼
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < 8; i++)
                {
                    sb.Append(hashBytes[i].ToString("X2"));
                }
                
                // 格式化為 XXXX-XXXX-XXXX-XXXX 格式
                string code = sb.ToString();
                return $"{code.Substring(0, 4)}-{code.Substring(4, 4)}-{code.Substring(8, 4)}-{code.Substring(12, 4)}";
            }
        }
        
        /// <summary>
        /// 驗證授權密碼
        /// Validate license password
        /// </summary>
        /// <param name="password">用戶輸入的密碼 / Password entered by user</param>
        /// <returns>是否驗證成功 / Whether validation succeeded</returns>
        public bool ValidateLicense(string password)
        {
            if (string.IsNullOrEmpty(password))
            {
                IsLicensed = false;
                OnLicenseStatusChanged?.Invoke(false);
                return false;
            }
            
            // 生成預期的密碼
            string expectedPassword = GenerateExpectedPassword(DeviceCode);
            
            // 驗證
            bool isValid = password.Trim().ToUpper() == expectedPassword.ToUpper();
            
            if (isValid)
            {
                // 保存授權
                SaveLicense(password);
                IsLicensed = true;
                OnLicenseStatusChanged?.Invoke(true);
                Debug.Log("[DeviceLicense] 授權成功！License activated successfully!");
            }
            else
            {
                IsLicensed = false;
                OnLicenseStatusChanged?.Invoke(false);
                Debug.LogWarning("[DeviceLicense] 授權密碼無效！Invalid license password!");
            }
            
            return isValid;
        }
        
        /// <summary>
        /// 根據設備碼生成預期的密碼
        /// Generate expected password based on device code
        /// </summary>
        private string GenerateExpectedPassword(string deviceCode)
        {
            using (SHA256 sha256 = SHA256.Create())
            {
                // 使用設備碼和另一個鹽值生成密碼
                string combined = deviceCode + "License_Password_Salt_2024";
                byte[] hashBytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(combined));
                
                // 取第8-15個字節作為密碼 (索引8到15)
                // Take bytes at indices 8-15 as password
                StringBuilder sb = new StringBuilder();
                for (int i = 8; i < 16; i++)
                {
                    sb.Append(hashBytes[i].ToString("X2"));
                }
                
                string password = sb.ToString();
                return $"{password.Substring(0, 4)}-{password.Substring(4, 4)}-{password.Substring(8, 4)}-{password.Substring(12, 4)}";
            }
        }
        
        /// <summary>
        /// 保存授權信息
        /// Save license information
        /// </summary>
        private void SaveLicense(string password)
        {
            // 加密保存
            string encrypted = EncryptString(password);
            PlayerPrefs.SetString(LICENSE_KEY, encrypted);
            PlayerPrefs.Save();
        }
        
        /// <summary>
        /// 檢查已保存的授權
        /// Check saved license
        /// </summary>
        private void CheckSavedLicense()
        {
            if (PlayerPrefs.HasKey(LICENSE_KEY))
            {
                string encrypted = PlayerPrefs.GetString(LICENSE_KEY);
                string decrypted = DecryptString(encrypted);
                
                if (!string.IsNullOrEmpty(decrypted))
                {
                    // 直接驗證密碼，不觸發保存和事件
                    // Directly validate password without triggering save and events
                    string expectedPassword = GenerateExpectedPassword(DeviceCode);
                    IsLicensed = decrypted.Trim().ToUpper() == expectedPassword.ToUpper();
                    
                    if (IsLicensed)
                    {
                        Debug.Log("[DeviceLicense] 已從保存的授權恢復。License restored from saved data.");
                    }
                }
            }
        }
        
        /// <summary>
        /// 清除授權
        /// Clear license
        /// </summary>
        public void ClearLicense()
        {
            PlayerPrefs.DeleteKey(LICENSE_KEY);
            PlayerPrefs.Save();
            IsLicensed = false;
            OnLicenseStatusChanged?.Invoke(false);
            Debug.Log("[DeviceLicense] 授權已清除。License cleared.");
        }
        
        /// <summary>
        /// 獲取加密用的密鑰
        /// Get encryption key
        /// </summary>
        private byte[] GetEncryptionKey()
        {
            string deviceId = GetDeviceIdentifier();
            string keyStr = deviceId.Substring(0, Math.Min(16, deviceId.Length)).PadRight(16, 'X');
            return Encoding.UTF8.GetBytes(keyStr);
        }
        
        /// <summary>
        /// 簡單的字符串加密
        /// Simple string encryption
        /// </summary>
        private string EncryptString(string text)
        {
            byte[] textBytes = Encoding.UTF8.GetBytes(text);
            byte[] keyBytes = GetEncryptionKey();
            
            for (int i = 0; i < textBytes.Length; i++)
            {
                textBytes[i] = (byte)(textBytes[i] ^ keyBytes[i % keyBytes.Length]);
            }
            
            return Convert.ToBase64String(textBytes);
        }
        
        /// <summary>
        /// 簡單的字符串解密
        /// Simple string decryption
        /// </summary>
        private string DecryptString(string encrypted)
        {
            try
            {
                byte[] encryptedBytes = Convert.FromBase64String(encrypted);
                byte[] keyBytes = GetEncryptionKey();
                
                for (int i = 0; i < encryptedBytes.Length; i++)
                {
                    encryptedBytes[i] = (byte)(encryptedBytes[i] ^ keyBytes[i % keyBytes.Length]);
                }
                
                return Encoding.UTF8.GetString(encryptedBytes);
            }
            catch
            {
                return null;
            }
        }
    }
}
