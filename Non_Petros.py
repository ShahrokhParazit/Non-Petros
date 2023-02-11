
from telethon import TelegramClient , events , Button
import time , requests , os , random , sys , psutil , platform , multiprocessing
from telethon import functions, types
from urllib.parse import urlparse
os.system("title Self_shahrokh")
#-------------------------------------------------------------------

api_id = 9031426
api_hash = '519feb4052933960f6fea9d6995a6fa6'
client = TelegramClient("shahrokh", api_id, api_hash).start()
print("         Self Runned")
admin = 5020604688
STATUS = True
BOLD = False
WRITER = False
ITALIC = False
STRIKE = False
DENIED = ['/id', '/ping', '/time', '/mute', '/unmute', '/cleanmute', '/porn', '/ip <host>', '/on', '/off', '/italic on', '/bold on', '/writer on', '/strike on', '/italic off', '/bold off', '/writer off', '/strike off', '/spam1 <count> <Text>', '/spam2 <count> <Text>', '/shot1 <website>', '/shot2 <website>', '/fosh1 <count>', '/fosh2 <count> <username/id>', '/fosh3 <count> <TEXT>', '/mydelete <count/max=4000>', '/delete <count/max=100>', '/enemy', '/delenemy']
mute_list = []
enemy_list = []
FOSH = open("fosh.txt",encoding="utf-8").readlines()


def regex_cc(text):
    try:
        card = re.findall("[0-9]{16}",text)[0]
        text1 = text.replace(card,"")
        date = re.findall('..\/..',text1)[0]
        text1 = text1.replace(date,"")
        cvv = re.findall(r'[0-9]{3}',text1)[0]
        return {"card":card,"date":date,"cvv":cvv}
    except:
        card = text.split("|")[0]
        date = text.split("|")[1]+"/"+text.split("|")[2]
        cvv = text.split("|")[3]
        return {"card":card,"date":date,"cvv":cvv}

def check_cc(cc_list):
    result=""
    for i in cc_list:
        try:
            cc = regex_cc(i)
            fix_card = cc['card'][:4]+"+"+cc['card'][4:8]+"+"+cc['card'][8:12]+"+"+cc['card'][12:16]
            data = "time_on_page=1080400&pasted_fields=number%2Czip&guid=NA&muid=f4d48849-7e13-4640-b065-cac94973692874a7ee&sid=249b36de-691b-410e-8458-5cd8bd46901f63a13a&key=pk_live_CUQtlpQUF0vufWpnpUmQvcdi&payment_user_agent=stripe.js%2F7315d41&card[number]="+fix_card+"&card[cvc]="+cc['cvv']+"&card[name]=Michael+S.+Walker&card[address_line1]=1835++College+Avenue&card[address_line2]=&card[address_city]=TULSA&card[address_state]=OK&card[address_zip]=74192&card[address_country]=US&card[exp_month]="+str(int(cc['date'].split("/")[0]))+"&card[exp_year]="+cc['date'].split("/")[1]
            headers = {"Accept" :"application/json", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://js.stripe.com", "Referer": "https://js.stripe.com/v2/channel.html?stripe_xdm_e=https%3A%2F%2Fdiscord.com&stripe_xdm_c=default509095&stripe_xdm_p=1"}

            r = requests.post("https://api.stripe.com/v1/tokens",headers=headers,data=data,timeout=2)
            try:
                ll = r.json()['card']['exp_month']
                result += "[✅] "+i+"\n"
            except:
                result += "[❌] "+i+"\n"
        except:
            result += "Error.\n"
        
    
    return result+"\n\nCC Checker By { @Difalio }"
#-------------------------------------------------------------------
@client.on(events.NewMessage(pattern="بصب"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        message = await event.get_reply_message()
        download= await client.download_media(message)
        await client.send_message("me",file=download)
        #os.remove(download)

@client.on(events.NewMessage(pattern="/ping"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        start = time.time()
        requests.get("https://google.com")
        ping = str(round( time.time() - start,4) )
        await event.edit(f"𝑷𝒊𝒏𝒈 **:** __{ping}__")

@client.on(events.NewMessage(pattern="/help"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        t= """𝐔𝐬𝐞𝐫 𝐁𝐨𝐭 𝐇𝐞𝐥𝐩 :

- /id : get user id with reply or in pv
- /ping : real server ping 
- /time : Now Time
- /mute : Mute with reply or in pv
- /unmute : Unmute with reply or in pv
- /cleanmute : clean mute list
- /porn : Randomly Porn from database
- /ip <host> : full host info 
- /on : Turn user bot on
- /off : Trun user bot off
- /italic on : Turn italic mode on
- /bold on : Turn Bold mode on
- /writer on : Turn Writer mode on
- /strike on : Turn Strike mode on
- /italic off : Turn italic mode off
- /bold off : Turn Bold mode off
- /writer off : Turn Writer mode off
- /strike off : Turn Strike mode off
- /spam1 <count> <Text> : spam text in lines
- /spam2 <count> <Text> : spam text in one line 
- /spam3 <count> <Text> : spam text and reply 
- /shot1 <website> : screenshot from website ( compressed image )
- /shot2 <website> : screenshot from website ( not compressed image )
- /fosh1 <count> : kosnane taraf with reply
- /fosh2 <count> <username/id> : kosnane taraf with username
- /fosh3 <count> <TEXT>
- /mydelete <count/max=4000> : delete own message 
- /delete <count/max=100> : delete chat message
- /enemy : enemy with reply or in pv
- /delenemy : delete enemy with reply or in pv
- /report <link/example https://t.me/1234/1234> <count/max=200> <type porn or other> : report with link
- /cc-check txt & file : reply
- /usage

𝐂𝐨𝐝𝐞𝐝 𝐁𝐲 : @Difalio"""
        await event.edit(t)
@client.on(events.NewMessage(pattern="/id"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        try:
            message = await event.get_reply_message()
            await event.edit("𝑰𝑫 **:** `"+str(message.from_id.user_id)+'`')
        except:
            chat = await event.get_chat()
            await event.edit("𝑰𝑫 **:** `"+str(chat.id)+'`')

@client.on(events.NewMessage(pattern="/report"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        try:
            
            link = event.text.split(" ")[1]
            count = int(event.text.split(" ")[2])
            type = event.text.split(" ")[3]
            username = link.split("t.me/")[1].split("/")[0]
            ids = link.split(username)[1].replace("/","")
            a1 = await event.edit("𝑹𝒆𝒑𝒐𝒓𝒕𝒊𝒏𝒈...")
            for i in range(count):
                if type.lower() == "porn":
                    try:
                        await client(functions.messages.ReportRequest(peer=username,id=[int(ids)],reason=types.InputReportReasonPornography()))
                    except:
                        pass
                elif type.lower()== "other":
                    try:
                        await client(functions.messages.ReportRequest(peer=username,id=[int(ids)],reason=types.InputReportReasonViolence()))
                    except:
                        pass
            await a1.edit(f"{str(count)} 𝑹𝒆𝒑𝒐𝒓𝒕 𝒘𝒂𝒔 𝑺𝒆𝒏𝒕 𝑻𝒐 𝑳𝒊𝒏𝒌 .")
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 ,  𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 . /report <link/example https://t.me/1234/1234> <count/max=200> <type porn or other>")
            
@client.on(events.NewMessage(pattern="/off"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        STATUS = False
        await event.edit("𝑼𝒔𝒆𝒓 𝒃𝒐𝒕 𝒕𝒖𝒓𝒏𝒆𝒅 𝒐𝒇𝒇.")

@client.on(events.NewMessage(pattern="/on"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == False:
        STATUS = True
        await event.edit("𝑼𝒔𝒆𝒓 𝒃𝒐𝒕 𝒕𝒖𝒓𝒏𝒆𝒅 𝒐𝒏.")

@client.on(events.NewMessage(pattern="/spam1"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        try:
            count = int(event.text.split(" ")[1])
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒏𝒖𝒎𝒃𝒆𝒓. /spam1 <count> <Text>")
        try:
            text = event.text.split("/spam1 "+str(count)+" ")[1]
            for i in range(count):
                await event.respond(text)
            await event.delete()
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 ,  𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒕𝒆𝒙𝒕. /spam1 <count> <Text>")

@client.on(events.NewMessage(pattern="/spam2"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        text2 = ""
        try:
            count = int(event.text.split(" ")[1])
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒏𝒖𝒎𝒃𝒆𝒓. /spam2 <count> <Text>")
        try:
            text = event.text.split("/spam2 "+str(count)+" ")[1]
            for i in range(count):
                text2 += text+"\n"

            await event.respond(text2)
            await event.delete()
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 ,  𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒕𝒆𝒙𝒕. /spam2 <count> <Text>")
@client.on(events.NewMessage(pattern="/spam3"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        try:
            count = int(event.text.split(" ")[1])
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒏𝒖𝒎𝒃𝒆𝒓. /spam3 <count> <Text>")
        try:
            text = event.text.split("/spam3 "+str(count)+" ")[1]
            for i in range(count):
                await event.respond.reply_message(text)
            await event.delete()
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 ,  𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒕𝒆𝒙𝒕. /spam3 <count> <Text>")
@client.on(events.NewMessage(pattern="/ip"))
async def Start(event):
    global admin , STATUS
    try:
        if event.sender_id == admin and STATUS == True:
            hostname = event.text.split(' ')[1]
            if "http" in hostname:
                hostname = urlparse(hostname).netloc

            response = requests.get('http://ip-api.com/json/'+hostname)
            response = response.json()
            status = response['status']
            country = response['country']
            regionName = response['regionName']
            city = response['city']
            isp = response['isp']
            ip = response['query']
            await event.edit('ᴅᴏᴍᴀɪɴ : **'+hostname.capitalize()+'**\nɪᴘ : **'+ip+'**\nᴄᴏᴜɴᴛʀʏ : **'+country+'**\nʀᴇɢɪᴏɴ : **'+regionName+'**\nᴄɪᴛʏ : **'+city+'**\nɪsᴘ : **'+isp+'**')
    except:
        await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒉𝒐𝒔𝒕. /ip <host>")
    
@client.on(events.NewMessage(pattern="/shot1"))
async def Start(event):
    global admin , STATUS
    try:
        if event.sender_id == admin and STATUS == True:
            try:
                url = event.text.split(" ")[1]
                a1 = await event.edit("𝑻𝒂𝒌𝒊𝒏𝒈 𝒔𝒄𝒓𝒆𝒆𝒏𝒔𝒉𝒐𝒕...")
            except:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒘𝒆𝒃𝒔𝒊𝒕𝒆. /shot2 <website>")
            r1 = requests.get("http://mini.site-shot.com/x/codebazan.ir-Web-screenshot/1000/png/?"+url,timeout=6)
            open("cap.jpg",'wb').write(r1.content)
            await a1.delete()
            await event.respond(f"𝑺𝒄𝒓𝒆𝒆𝒏𝒔𝒉𝒐𝒕 𝒇𝒓𝒐𝒎 [link]({url}).\n\n𝑷𝒐𝒘𝒆𝒓𝒆𝒅 𝒃𝒚 : `@Difalio`",file="cap.jpg")
            
            os.remove("cap.jpg")
    except:
        await event.edit("𝑼𝒏𝒆𝒙𝒑𝒆𝒄𝒕𝒆𝒅 𝒆𝒓𝒓𝒐𝒓.")

@client.on(events.NewMessage(pattern="/cc-check"))
async def Start(event):
    global admin , STATUS
    try:
        if event.sender_id == admin and STATUS == True:
            a1 = await event.edit("Check started...")
            try:
                
                mess = await event.get_reply_message()
                download = await client.download_media(mess)
                cc_lis = open(download,encoding="utf-8").read().replace("\r","").split("\n")
                os.remove(download)
                mmm = check_cc(cc_lis)
                await a1.edit(mmm)
            except:
                mess = await event.get_reply_message()
                mmm = check_cc(mess.text.split("\n"))
                await a1.edit(mmm)
    except:
        await event.edit("𝑼𝒏𝒆𝒙𝒑𝒆𝒄𝒕𝒆𝒅 𝒆𝒓𝒓𝒐𝒓.")

@client.on(events.NewMessage(pattern="/usage"))
async def Start(event):
    global admin , STATUS
    try:
        if event.sender_id == admin and STATUS == True:
            memory = psutil.virtual_memory()[2]
            cpus = psutil.cpu_percent()
            system_name = platform.platform()
            processor = platform.processor()
            os_version = platform.version()
            totallcpu = multiprocessing.cpu_count()
            totall = str(psutil.virtual_memory()[0] / (1024**3))[:4]
            text = """
CPU Usage : {}%
RAM Usage : {}%
CPU Core Count : {}
Total RAM : {} GB
OS : {}
Processor : {}
OS version : {}
            """.format(cpus, memory, totallcpu, totall,system_name,processor,os_version)
            await event.edit(text)
    except:
        await event.edit("𝑼𝒏𝒆𝒙𝒑𝒆𝒄𝒕𝒆𝒅 𝒆𝒓𝒓𝒐𝒓.")
                
@client.on(events.NewMessage(pattern="/shot2"))
async def Start(event):
    global admin , STATUS
    try:
        if event.sender_id == admin and STATUS == True:
            try:
                url = event.text.split(" ")[1]
                a1 = await event.edit("𝑻𝒂𝒌𝒊𝒏𝒈 𝒔𝒄𝒓𝒆𝒆𝒏𝒔𝒉𝒐𝒕...")
            except:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒘𝒆𝒃𝒔𝒊𝒕𝒆. /shot2 <website>")
            r1 = requests.get("http://mini.site-shot.com/x/codebazan.ir-Web-screenshot/1000/png/?"+url,timeout=6)
            open("cap.jpg",'wb').write(r1.content)
            await a1.delete()
            await event.respond(f"𝑺𝒄𝒓𝒆𝒆𝒏𝒔𝒉𝒐𝒕 𝒇𝒓𝒐𝒎 [link]({url}).\n\n𝑷𝒐𝒘𝒆𝒓𝒆𝒅 𝒃𝒚 : `@Difalio`",file="cap.jpg",force_document=True)
            
            os.remove("cap.jpg")
    except:
        await event.edit("𝑼𝒏𝒆𝒙𝒑𝒆𝒄𝒕𝒆𝒅 𝒆𝒓𝒓𝒐𝒓.")

@client.on(events.NewMessage(pattern="/fosh1",func=lambda e:e.is_reply))
async def Start(event):
    global admin , STATUS , FOSH
    if event.sender_id == admin and STATUS == True:
        try:
            chat = await event.get_chat()
            message = await event.get_reply_message()
            count = int(event.text.split("/fosh1 ")[1])
            await event.delete()
            for i in range(count):
                await client.send_message(chat.id,random.choice(FOSH),reply_to=message.id)
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒏𝒖𝒎𝒃𝒆𝒓. /fosh1 <count>")

@client.on(events.NewMessage(pattern="/fosh2"))
async def Start(event):
    global admin , STATUS , FOSH
    if event.sender_id == admin and STATUS == True:
            try:
                count = int(event.text.split(" ")[1])
            except:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒏𝒖𝒎𝒃𝒆𝒓. /fosh2 <count> <username/id>")
                requests.get("asds")
            try:
                text = event.text.split("/fosh2 "+str(count)+" ")[1]
            except:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝑼𝒔𝒆𝒓. /fosh2 <count> <username/id>")
                requests.get("asds")
            await event.delete()
            if "@" in text:
                for i in range(count):
                    await event.respond(random.choice(FOSH)+"\n"+text)
            elif text.isnumeric():
                for i in range(count):
                    await event.respond(random.choice(FOSH)+"\n[bala bash binamus](tg://user?id="+text+")")
            else:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝑼𝒔𝒆𝒓. /fosh2 <count> <username/id>")
@client.on(events.NewMessage(pattern="/fosh3"))
async def Start(event):
    global admin , STATUS , FOSH
    if event.sender_id == admin and STATUS == True:
            try:
                count = int(event.text.split(" ")[1])
            except:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒏𝒖𝒎𝒃𝒆𝒓. /fosh3 <count> <username/id>")
                requests.get("asds")
            try:
                text = event.text.split("/fosh3 "+str(count)+" ")[1]
            except:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝑼𝒔𝒆𝒓. /fosh3 <count> <username/id>")
                requests.get("asds")
            await event.delete()
            for i in range(count):
                    await event.respond(random.choice(FOSH)+"\n"+text)
            else:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝑼𝒔𝒆𝒓. /fosh3 <count> <TEXT>")
@client.on(events.NewMessage(pattern="/porn"))
async def Start(event):
    global admin , STATUS 
    if event.sender_id == admin and STATUS == True:
        messages=await client.get_messages("selfp0rno",limit=int(456))
        mm = random.choice(messages)
        timee1 = str(round(mm.document.attributes[0].duration / 60,2)).split(".")[0]
        timee2 = str(round(mm.document.attributes[0].duration / 60,2)).split(".")[1]
        if len(list(timee1)) != 2:
            timee1 = "0"+timee1
        elif len(list(timee2)) != 2:
            timee2 = "0"+timee2

        mm.text = "𝒀𝒐𝒖𝒓 𝒑𝒐𝒓𝒏 𝒓𝒆𝒒𝒖𝒆𝒔𝒕 𝒓𝒆𝒔𝒖𝒍𝒕.\n\n𝑽𝒊𝒅𝒆𝒐 𝑽𝒐𝒍𝒖𝒎𝒆 : "+str(round(mm.document.size / 1000000,2))+" MB\n"+"𝑫𝒖𝒓𝒂𝒕𝒊𝒐𝒏 : "+timee1+":"+timee2+" min"+"\n\n𝑷𝒐𝒘𝒆𝒓𝒆𝒅 𝒃𝒚 : `@Difalio`"
        await event.respond(mm)
@client.on(events.NewMessage(pattern="/mydelete"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        try:
            group = await event.get_chat()
            group = int("-100" + str(group.id))
            count = event.text.split(" ")[1]
            if int(count) <= 4000:
            
                messages=await client.get_messages(group,limit=int(count))
                for a in messages:
                    try:
                        if a.from_id.user_id == admin:
                            await client.delete_messages(group,a.id)

                    except:
                        pass
            else:
                await event.edit("𝒀𝒐𝒖 𝑪𝒂𝒏'𝒕 𝒅𝒆𝒍𝒆𝒕𝒆 𝒎𝒐𝒓𝒆 𝒕𝒉𝒂𝒏 4000.")
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒏𝒖𝒎𝒃𝒆𝒓. /mydelete <count>")

@client.on(events.NewMessage(pattern="/mute"))
async def Start(event):
    global admin , STATUS , mute_list
    if event.sender_id == admin and STATUS == True:
        try:
            message = await event.get_reply_message()
            mute_list.append(message.from_id.user_id)
            await event.edit("𝑴𝒖𝒕𝒆𝒅.")
        except:
            chat = await event.get_chat()
            mute_list.append(chat.id)
            await event.edit("𝑴𝒖𝒕𝒆𝒅.")

@client.on(events.NewMessage(pattern="/unmute"))
async def Start(event):
    global admin , STATUS , mute_list
    if event.sender_id == admin and STATUS == True:
        try:
            message = await event.get_reply_message()
            mute_list.remove(message.from_id.user_id)
            await event.edit('𝑼𝒏𝒎𝒖𝒕𝒆𝒅.')
        except:
            chat = await event.get_chat()
            mute_list.remove(chat.id)
            await event.edit("𝑼𝒏𝒎𝒖𝒕𝒆𝒅.")

@client.on(events.NewMessage(pattern="/cleanmute"))
async def Start(event):
    global admin , STATUS , mute_list
    if event.sender_id == admin and STATUS == True:
        mute_list = []
        await event.edit("𝑴𝒖𝒕𝒆 𝑳𝒊𝒔𝒕 𝑪𝒍𝒆𝒂𝒏𝒆𝒅.")

@client.on(events.NewMessage(pattern="/time"))
async def Start(event):
    global admin , STATUS , mute_list
    if event.sender_id == admin and STATUS == True:
        try:
            r = requests.get("http://api.codebazan.ir/time-date/?json=all",timeout=5).json()
            t = f"""{r['result']['dateen']} ~ {r['result']['timeen']}
{r['result']['datefa']} ~ {r['result']['timefa']}

𝑷𝒐𝒘𝒆𝒓𝒆𝒅 𝒃𝒚 : ` @Difalio`"""
            await event.edit(t)
        except:
            await event.edit("𝑼𝒏𝒆𝒙𝒑𝒆𝒄𝒕𝒆𝒅 𝒆𝒓𝒓𝒐𝒓.")

@client.on(events.NewMessage(pattern="/delete"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:  
        try:
            chat = await event.get_chat()
            mes = int(event.text.split("/delete ")[1])
            now = event.id + 1
            end = now - mes
            await client.delete_messages(chat.id,[i for i in range(end,now)])  
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒏𝒖𝒎𝒃𝒆𝒓. /delete <count>")

@client.on(events.NewMessage(pattern="/enemy"))
async def Start(event):
    global admin , STATUS , enemy_list
    if event.sender_id == admin and STATUS == True:  
        try:
            message = await event.get_reply_message()
            enemy_list.append(message.from_id.user_id)
            await event.edit('𝑨𝒅𝒅𝒆𝒅 𝑻𝒐 𝑬𝒏𝒆𝒎𝒚.')
        except:
            chat = await event.get_chat()
            enemy_list.append(chat.id)
            await event.edit("𝑨𝒅𝒅𝒆𝒅 𝑻𝒐 𝑬𝒏𝒆𝒎𝒚.")

@client.on(events.NewMessage(pattern="/delenemy"))
async def Start(event):
    global admin , STATUS , enemy_list
    if event.sender_id == admin and STATUS == True:  
        try:
            message = await event.get_reply_message()
            enemy_list.remove(message.from_id.user_id)
            await event.edit('𝑹𝒆𝒎𝒐𝒗𝒆𝒅 𝒇𝒓𝒐𝒎 𝑬𝒏𝒆𝒎𝒚.')
        except:
            chat = await event.get_chat()
            enemy_list.remove(chat.id)
            await event.edit("𝑹𝒆𝒎𝒐𝒗𝒆𝒅 𝒇𝒓𝒐𝒎 𝑬𝒏𝒆𝒎𝒚.")

@client.on(events.NewMessage())
async def Bold(event):
    global admin , STATUS , BOLD , WRITER , ITALIC , STRIKE , mute_list , enemy_list , FOSH , DENIED
    if event.sender_id == admin and STATUS == True and event.text.lower() == "/bold on":
        BOLD = True
        await event.edit("𝑩𝒐𝒍𝒅 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒏.")
    elif event.sender_id == admin and STATUS == True and event.text.lower() == "/bold off":
        BOLD = False
        await event.edit("𝑩𝒐𝒍𝒅 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒇𝒇.")
    elif event.sender_id == admin and STATUS == True and event.text.lower() == "/writer on":
        WRITER = True
        await event.edit("𝑾𝒓𝒊𝒕𝒆𝒓 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒏.")
    elif event.sender_id == admin and STATUS == True and event.text.lower() == "/writer off":
        WRITER = False
        await event.edit("𝑾𝒓𝒊𝒕𝒆𝒓 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒇𝒇.")
    elif event.sender_id == admin and STATUS == True and event.text.lower() == "/italic on":
        ITALIC = True
        await event.edit("𝑰𝒕𝒂𝒍𝒊𝒄 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒏.")
    elif event.sender_id == admin and STATUS == True and event.text.lower() == "/italic off":
        ITALIC = False
        await event.edit("𝑰𝒕𝒂𝒍𝒊𝒄 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒇𝒇.")
    elif event.sender_id == admin and STATUS == True and event.text.lower() == "/strike on":
        STRIKE = True
        await event.edit("𝑺𝒕𝒓𝒊𝒌𝒆 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒏.")
    elif event.sender_id == admin and STATUS == True and event.text.lower() == "/strike off":
        STRIKE = False
        await event.edit("𝑺𝒕𝒓𝒊𝒌𝒆 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒇𝒇.")
    elif event.sender_id == admin and STATUS == True and BOLD == True  and event.text.lower() != "/bold off" and event.text.lower() != "/strike on" and event.text.lower() != "/strike off" and event.text.lower() != "/writer on" and event.text.lower() != "/writer off" and event.text.lower() != "/italic on" and event.text.lower() != "/italic off" and event.text.lower() != "/off" and event.text.lower() != "/on":
        await event.edit("**"+event.text+"**")
    elif event.sender_id == admin and STATUS == True and WRITER == True and event.text.lower() != "/bold off" and event.text.lower() != "/strike on" and event.text.lower() != "/strike off" and event.text.lower() != "/writer on" and event.text.lower() != "/writer off" and event.text.lower() != "/italic on" and event.text.lower() != "/italic off" and event.text.lower() != "/off" and event.text.lower() != "/on":
        await event.edit("`"+event.text+"`")
    elif event.sender_id == admin and STATUS == True and ITALIC == True and event.text.lower() != "/bold off" and event.text.lower() != "/strike on" and event.text.lower() != "/strike off" and event.text.lower() != "/writer on" and event.text.lower() != "/writer off" and event.text.lower() != "/italic on" and event.text.lower() != "/italic off" and event.text.lower() != "/off" and event.text.lower() != "/on":
        await event.edit("__"+event.text+"__")
    elif event.sender_id == admin and STATUS == True and STRIKE == True and event.text.lower() != "/bold off" and event.text.lower() != "/strike on" and event.text.lower() != "/strike off" and event.text.lower() != "/writer on" and event.text.lower() != "/writer off" and event.text.lower() != "/italic on" and event.text.lower() != "/italic off" and event.text.lower() != "/off" and event.text.lower() != "/on":
        await event.edit("~~"+event.text+"~~")
    elif event.sender_id in mute_list:
        await event.delete()
    elif event.sender_id in enemy_list:
        await event.reply(random.choice(FOSH))
client.run_until_disconnected()
