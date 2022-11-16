from TikTokApi import TikTokApi

verifyFp="verify_YOUR_S_V_WEB_ID_COOKIE"
api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
print(api.trending(count=1))