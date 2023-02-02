import requests

import re

filename = input("filename (out.txt) :>")
if not filename:
  filename = "out.txt"

def parse_and_send_request(instring, page_num):
    # Split the input string into lines
    lines = instring.split("\n")
        
    # Extract the URL from the first line
    url = lines[0].split("'")[1]
    
    # Initialize the headers dictionary
    headers = {}
    
    # Loop through the remaining lines and extract the header key-value pairs
    for line in lines[1:]:
        #key, value = line.split(": ")[1:]

        match = re.search(r"^\s*-H\s+'([^']+):\s+(.+)'", line)
        if match:
          key, value = match.group(1), match.group(2)
          # rest of the code here
        #else:
        #  # raise an error or handle the case in some other way
        #  print(f"disregard {line}")

        headers[key] = value.strip()
    
    # Send the HTTP request using the requests library
    if page_num:
      url = url + f"&page={page_num}" 
    response = requests.get(url, headers=headers)
    
    # Return the response as a string
    return response.text

default_i = """curl 'https://www.midjourney.com/api/app/recent-jobs/?amount=50&jobType=null&orderBy=new&user_id_ranked_score=null&jobStatus=completed&userId=502314761027977252&dedupe=true&refreshApi=0' \
  -H 'authority: www.midjourney.com' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9,ru;q=0.8' \
  -H 'cookie: __stripe_mid=cb898425-c075-45da-866b-68000613c4718c6fa6; _ga=GA1.1.108234462.1661361270; imageSize=medium; imageLayout_2=hover; getImageAspect=3; fullWidth=false; showHoverIcons=true; __Host-next-auth.csrf-token=e06d41bc68c55a938df6bd9b6eb3822c25196ee6c882842130e441afe0e59533%7Cd116e27faf8fe5393537decdf5231616102a2a125175169c8a224fd235faa54c; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.midjourney.com; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..KeGbhSdp5IXqzuSn.lUJGzcUqyjn_XFyDpb1HRexIVjA2PCuQmiW4qYg3vQ0w-V6GTuDgLDunlTOAKCDtsPTXs1wsx16aAx7u6wTMr3C2RVZlSj9TM_qIEs2oMycz0vrMFAJ5Q-kIHSkXW1e62n0lUt_lvWVjWYMuglaZyvq8tPhTNAUwunizUB3Uh2G02KR7AvW-mPrRcc-pJQUsMc58GhdMgpD13IEgRO9-KNfww2WFn50DQqVLwC_IfZDB73QnW3lZj8oaIvMmbBMPgi6jW0V8lWVG8SMarB6De-I1FR4RM1C9_jWl9MFr99Ntf0dD9qVkndsbmfCK62UtyVCm0HNmrXNHjM2PdkMMS45j9099HSl7k7dbgEGwcp8sY6EiidlZoeQh4t-yv4jO_3Z7nAFF6H1kyTfjWJH_zVXUM6MZJ_H2MMwocQlXjHKuTG8ZU9kDuFiqnwaIcxxLx_rE9FtvTuG9bRaLCFVQ4E0pPdBEdbjhmkUT3myyy7CzuHrttFd037wxa45oDwAjB5-wlLdFnCdTrrxjZ-0P0BUGGpXeEl-5zBA572JTWOXIfOu4KmmzVcd9eaIaXlhr5sArSq5LkBVSKKSiT7tgl-ebzB1nMmdskzIi0P-6uDQ_p1O_IiL7jHsv7OwjUqWhgJhvt0GmFCvJs4uKeE2is3KvoHMAocsTED5_T2H13_lzcrbMzeNsctbPV26OSAlg0auNKYsK-D-FYD5LGt8xgziw2ucpd5nnkEd51SPg423nZSeFLOrgSHWqHn8qlviYgY808GAr9z7THP7VBO6uSqOQ47EhpXmAvAS4oJz68juKaWL3C922xdcctTrH_GfvsOQb-uB1Dd_gFvlUPnlLRS7fgMa1eWPvszqI6yWSi8tu_2UNU2VuKJ90_fil5e1o4qs2xkyZDY9tVJj7Wu6qt8HOcOiQTCOjJfTCSu6DQWbsWkJYID1GZXHAnuUK18I82WqGZJC8tprntVv95UHbgnuG4DVSqhFshvpwMP1q0QawZTRxT1wYxZY8dzfzH85gm0fXKyvcAIzGN9YbPwFhzvXoZderF2CcEAqP38IyFoyBSHQjQcBL2MMNS66dWonia2rcDTXTWkdAiu1CQqaOGAK2W8nYh6py2dpIkuq5Sn8eu85A_2b2g_mcOlp0T_dVy41_1VWd6gwdNtkZoo13Dvy__6Su-PWiYrZ_h3B5K2wQ8PZNfLZNs4QG1J_7C6bJKoonytOlekZ7dXCJv79wnCYNlb--3H1XRKrNHuwFsUNjJFZUW5iVDRLUz_oQd5j23m484_eOh2fC_q1rw6S2i8cuexA1l5W-zFk-glvEqfQgzJK7oAQ1UJBK5V-9UdsLvRbjxhFn07WaLNnlINcXWpbKHkR9IGuikThSUhCBne1j_SEWwWYA7BeZTlTNtfNdxhJXsXlHlVh2HzY7hKc1JvM94t8SkErfTCM1lVolVCAPZHf6ssANWncjoiJSeU3LIpss2ODEgTq6vFU9LZzn9PYM1jiUWLtdUVda0mgwRYX9oii-rwCuBVeaW7-0VIV-ZKGx34dmrU9syZnNwb8si7ZatsexH5C8A5tvrnZ4qkP0Mq4djiktA5PWWHwZvGeOmLn5328jj5lioPp8TTYjjm7NSxQRdqkL42vwlmCkJ3Rrbu5oS5Z8r5l1eRwv5Ht6v-VomPM9JJVYIWNj3moIuipnyFXiRPNFOGg8Sskmh2Wzrkzt1a4aGe0BBVHQhlJWz_gDsoUHTTLdKqfBshTW6EakQ11yfk8pgNCRqjxFsoRiSRoDYa2eh_Bqw-nckppN7dxFuaSxtRQOpsKhnl2YQC9UWdjJW029Bzl7PkUJPkM_VGIPFpf_YkN5YlxqdtAWABtozPgHgzib79eIt1wuYU58mGhfbcQvVg1ZUKvyQvMVZYos91yEcYYuOjac9r_XTQ0Ixi30Tq9zme3VodkSGZOD8lfCPG7E1DHNyGl9yubI_dZWIGsrVCbobKLRRLCTWLpVTOgGixOeTEWIUVsheH2_pglHSF2xLVBPhuYSGM2hnypNXl1VTdlVbBPDKWwRcF4ya2eX8Q6edVvr0TIKqlvqJoLsvaf4DQMMeO4iJHCXsltXoq0vUCEHKpr1FMnQR9n5byStau9f-VsuTx9sJWgiaQ8KXeAw6KHHYxAryWQ-n3s1mWYTH-0jHtvMvEbm_brGcVwSyCILupLg_FEn6Xhp0EerRJzU8h9xBHFj0JnB-WxBYxMTmfDXPNxIDeN3ygGwjaxv8XwZx4Cfwt07wQgXxBun0gsn2DpUFUCxt422FZj5HwDzx_SgiMDjwIad4F1n4oCH1pobtCa9svkD_uoOxFDZdkFfz7EwXv2lmB93nwkfecV1mhrRrVq2Lq8CllVzcJiMux3YFK4MQxzb8ya1U0lbwcxUjPZ9rgxqZ9XsyClIaVWddPfnKkEryKutmlb2ImFgS5hOqRMRNO2xRGdLIhsbTWw_5yTZlbtXoozyd5y14vvSfFa1yYJUHjRoMZ2YOGyVTPbxoIH5xkdm2A2swYQ2ZMADGdzsWol5vIGi6PUUUC_SYZw0aaxOIzhnoMsq6t9NniF5aRPo4JffBI-5HmwXx81Gcakh8w7yp6raTiUYsONugFG790LC_pq3ba3_y_jSbu_Z2JvZuCFBTWt60BURuG1rT1EBWT9M3BNAxeBXUcWkL-3WDcjvpKf6lmVf6hrYxYBI5j31Pcr2jaUz5EmyRjqU_ZqrUxIweRQ7ztJ9EjhECltD9LcBH3r_O-k68uMiBGyMPztFZ8jNaT_XvzgiMLxcrIwlwnn4A8dW_R3IIhFTgskUsAjZalYjv1Mn1uiiEYUHp2nW6Jmz1pKQLqzAlr9jwnqdQ4O3oii6lIcbNDgxyEqqgCs.CHzOLhOaWw8OB1pHubnWfQ; _ga_Q0DQ5L7K0D=GS1.1.1675316174.135.0.1675316174.0.0.0; _dd_s=rum=0&expire=1675317075119' \
  -H 'referer: https://www.midjourney.com/app/' \
  -H 'sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' \
  --compressed"""
i = ""
while True:
  instr = ""
  instr = input(":> ")
  i = i + instr + "\n"
  if instr[len(instr)-1] != '\\':
    break

fl = open(filename, 'w')

import json
def get_mj(i, page_num):
  print(f"Extracting and executing curl command: Page {page_num}")
  contents = parse_and_send_request(i, page_num)
  j = json.loads(contents)
  cn = 0
  for k in j:
    if 'prompt' in k.keys():
      prom = k["prompt"]
      try:
        if prom is not None:
          fl.write(prom + "\n")
          cn = cn + 1
      except:
        continue
        #print(">>>>> " + prom[0:10])
  #print(x)
  return cn
if i.find("curl") != -1:
  count = 0
  for page in range(1,20):
    count = count + get_mj(i, page)
  print(f"{count} prompts")
else:
  print("Please enter a curl command")

fl.close()