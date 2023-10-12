流量分析里CobalStrike流量解密
	脚本
		1.CS_Decrypt：解密cookie
		2.cs-scripts：解密cs私钥
	流量特征
		1.CS会定期发送心跳包通常由四个数字或字母组成，例如GET /4Ekx HTTP/1.1
		2.木马访问攻击者C2服务器上的submit.php页面，并且在访问请求中带有一个id参数。这就是CS下发指令的特征之一
	解题步骤
		kali下
		1.导出流量包内key
		2.使用cs-scripts/parse_beacon_keys.py脚本解密key，得到公钥、私钥
		3.获取协商密钥，协商密钥由RSA公钥加密后放在心跳包的cookie中
			使用CS_Decrypt/Beacon_metadata_RSA_Decrypt.py脚本获取AES key和HMAC key
				脚本中添加私钥和cookie
		4.解密流量包内data
			1.wireshark使用原始数据导出16进制数据，使用CyberChef from hex解码后to Base64转为Base64编码
			2.使用Beacon_Task_return_AES_Decrypt.py脚本解密Base64编码
				脚本内SHARED_KEY和HMAC_KEY填入AES key和HMAC key