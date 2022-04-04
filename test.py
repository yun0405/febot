import discord
from discord.ext import commands
import random
import os
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def 갈통아(ctx):
    await ctx.send(f'반갑습니다.{ctx.author.mention}님 철갈통ver1.3 현재 상태 양호합니다.\n[로또]명령어가 추가되었습니다.')
    
@bot.command()
async def 철윤생일(ctx):
    await ctx.send(f'4월 5일이 주인놈 생일입니다') 
    
    
@bot.command()
async def 주인생일(ctx):
    await ctx.send(f'알게뭡니까')
    
    
@bot.command()
async def hello(ctx):
    embed = discord.Embed(title="안녕하세요", description=f'{ctx.author.mention}님 안녕하세요!',color=0x00ff00)
    await ctx.send(embed=embed)



@bot.command()
async def 주사위(ctx):
    await ctx.send(f'{random.randint(1,100)} 이가 나왔습니다.')

@bot.command()
async def 타로(ctx):
    match(random.randint(1,23)):
        case(1):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 00번 카드인 The fool(바보)카드 입니다.\n이 카드는 인생에서 새로운 세계로 첫 발을 내딛는 초보자이며 어이없는 실수에 대한 경고도 포함하고 있습니다.\n정방향 키워드는 시작,순수한,낙천적인입니다.\n역방향 키워드는 끝,멍청한 실수입니다.')
        case(2):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 01번 카드인 The magician(마법사)카드 입니다.\n이 카드의 가장 큰 의미는 무엇이든지 알고있는 사람이며 능력있는 사람을 뜻합니다.\n정방향 키워드는 힘,능력,해결사입니다.\n역방향 키워드는 무능령,불안정입니다. ')
        case(3):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 02번 카드인 The High Priestess(고위 여사제)카드 입니다.\n이 카드는 비밀스러움을 간직하고있는 카드입니다. 동시에 문서적으로 좋은일이 생길수도있습니다.\n정방향 키워드는 비밀,합격,종교입니다.\n역방향 키워드는 공격적,인내심이 부족한,얄팍한입니다.')
        case(4):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 03번 카드인 The Empress(여왕) 카드 입니다.\n이 카드는 여성스러움과 풍요로움을 상징하는 카드입니다.\n정방향 키워드는 풍요,여성스러움입니다.\n역방향 키워드는 가난,지연됨,탐욕,이해심없음입니다.')
        case(5):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 04번 카드인 The Emperor(황제) 카드 입니다.\n이 카드는 강한 가부장적인 카드이며, 권력과 카리스마를 나타내는 카드이기도 합니다.\n정방향 키워드는 권력,성공,독재입니다.\n역방향 키워드는 권력없음,의지빈약,허세,책임감이없음입니다.')
        case(6):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 05번 카드인 The Hierophant(교황) 카드 입니다.\n이 카드는 존경받는 사람을 상징하며, 개인적인 문제를 털어놓고 이야기할수 있는 사람이며 조언자의 역할을 하는 카드입니다.\n정방향 키워드는 가르침,교육,중개,규칙입니다.\n역방향 키워든는 독단적,규칙을 지키지 않음,인정받지 못한,얕은 지식 ')
        case(7):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 06번 카드인 The Lovers(연인) 카드 입니다.\n이 카드는 매력과 사랑을 나타내는 카드이며,두가지 선택지중에서의 선택을 암시하는 카드입니다.\n정방향 키워드는 사랑,선택,좋은 관계입니다.\n역방향 키워드는 이별,결별,배신,선택의 여지가 없음입니다. ')
        case(8):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 07번 카드인 The Chariot(전차) 카드 입니다.\n이 카드는 앞으로 나아가는 힘이 강한 진취적인 카드입니다. 하지만 힘을 잘 분배하지 않으면 계획이 삐걱거릴수도있습니다.\n정방향 키워드는 승리,이동,행동할때,자신감입니다.\n역방향 키워드는 패배,중간에 그만두게됨,균형이 어긋나기 시작,의지빈약입니다.')
        case(9):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 08번 카드인 The Strength(힘) 카드 입니다.\n이 카드는 외적인 힘이 아닌 내면의 힘을 나타내는 카드입니다. 강한 정신력과 인내가 필요한 시점입니다.\n정방향 키워드는 힘,정신력,인내입니다.\n역방향 난폭,허황됨,남용,인내심부족입니다.')
        case(10):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 09번 카드인 The Hermit(은둔자) 카드 입니다.\n이 카드는 세속을 스스로 떠난 은둔자 카드로 지적이며, 신중함을 나타내는 카드입니다.\n정방향 키워드는 지적인,고독,신중,경계,조언\n역방향 키워드는 경솔,미성숙,현식적입니다.')
        case(11):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 10번 카드인 Wheel Of Fortune(운명의 수레바퀴) 카드 입니다.\n이 카드는 새로운 시작과 더 나은 방향으로 전환을 뜻하는 카드입니다.\n정방향 키워드는 운명,좋은 변화,행운입니다.\n역방향 키워드는 곤경,원치않는 변화,불행,배신입니다.')
        case(12):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 11번 카드인 Justice(정의) 카드 입니다.\n이 카드는 균형과 조화를 나타내며, 어느 한쪽으로도 치우치지 않은 공명정대함을 뜻하는 카드입니다.\n정방향 키워드는 균형,공평,정직,책임입니다.\n역방향 키워드는 불공평,편파,편견,이기적입니다. ')
        case(13):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 12번 카드인 The Manged Man(매달린 남자) 카드 입니다.\n이 카드는 현실적으로 아무것도 할수없는 정체된 상태를 나타내는 카드입니다. 지금은 때가 아니니 때를 기다리시는게 좋을것 같습니다.\n정방향 키워드는 침체,시련,멈춤입니다.\n역방향 키워드는 안절부절,자기중심적입니다.')
        case(14):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 13번 카드인 The Death(죽음) 카드 입니다.\n이 카드는 죽음을 나타내는 카드로 뜻하지않은 변화로인해 안좋은 영향을 받을것을 암시하는 카드입니다.또한 끝과 새로운 시작이라는 뜻도 포함하고 있습니다.\n정방향 키워드는 불행,새로운 시작,뜻하지않은 큰 변화입니다.\n역방향 키워드는 침체,고통,고갈,무기력입니다.')
        case(15):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 14번 카드인 Temperance(절제) 카드 입니다.\n이 카드는 중용과 인내를 의미하는 카드입니다.변화에 흔들리지않고 감정을 잘 다스릴 필요가 있을것 같습니다.\n정방향 키워드는 절제,조화,교류입니다.\n역방향 키워드는 불화,인내심없음,이해심부족입니다.')
        case(16):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 15번 카드인 The Devil(악마) 카드 입니다.\n이 카드는 집착과 고통을 나타내며 채워지지 않는 욕망을 나타냅니다.\n정방향 키워드는 타락,지나친 탐욕,부정적,복종,속박된상태입니다.\n역방향 키워드는 벗어남,이별,자유로움입니다.')
        case(17):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 16번 카드인 The Tower(탑) 카드 입니다.\n이 카드는 커다란 변화를 암시하는 카드입니다. 계획이나 일이 뜻 밖의 사건으로 엉망이 될수도있습니다.\n정방향 키워드는 좋지 않은 변화,위기,폭로입니다.\n역방향 키워드는 좋지않은변화,불운의 연속,파산입니다.')
        case(18):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 17번 카드인 The Star(별) 카드 입니다.\n이 카드는 희망과 행운을 암시하는 카드이며, 긍정적인 결과와 행운과 재생을 나타내는 카드입니다.\n정방향 키워드는 희망,아이디어,사랑입니다.\n역방향 키워드는 절망,실망,이별입니다.')
        case(19):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 18번 카드인 The Moon(달) 카드 입니다.\n이 카드는 불확실성과 속임수등을 의미하는 카드입니다.\n정방향 키워드는 숨겨짐,불안한 관계,당황입니다.\n역방향 키워드는 위기모면입니다.')
        case(20):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 19번 카드인 The Sun(태양) 카드 입니다.\n이 카드는 22장의 메이저 카드중에 가장 긍정적이며, 행복하고 만족스러운 카드입니다.어떤 상황이나 사건, 목표에서 원하는 결과를 얻을수있을겁니다.:)\n정방향 키워드는 활기,행복,성공,만족,사랑입니다.\n역방향 키워드는 불확실성,불행,불안입니다')
        case(21):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 20번 카드인 Judgement(심판) 카드 입니다.\n이 카드는 지금까지의 과거를 통해 결단을 내려야할 때임을 나타내고있습니다.\n정방향 키워드는 결단을 내려야할 때,변화,재회입니다.\n역방향 키워드는 심판,낙방,헤어짐입니다. ')
        case(22):
            await ctx.send(f'반갑습니다.\n{ctx.author.mention}님이 뽑으신 카드는 21번 카드인 The World(세계) 카드 입니다.\n이 카드는 모든 단계의 완성을 나타내는 카드입니다.\n정방향 키워드는 완성,성공,이동입니다.\n역방향 키워드는 미완성,미숙,좌절입니다.')    
        case(23):
            await ctx.send(f'귀찮은데...')
@bot.command()
async def 할까(ctx):
    match(random.randint(1,2)):
        case(1):
            await ctx.send(f'해')
        case(2):
            await ctx.send(f'하지마')
@bot.command()
async def 거짓말(ctx):
    match(random.randint(1,2)):
        case(1):
            await ctx.send(f'삐빅 진실입니다.')
        case(2):
            await ctx.send(f'삐빅 거짓입니다.')            
            
@bot.command()
async def 방향(ctx):
    match(random.randint(1,2)):
        case(1):
            await ctx.send(f'정방향입니다.')
        case(2):
            await ctx.send(f'역방향입니다.') 
            
@bot.command()
async def 깡(ctx):
    match(random.randint(1,7)):
        case(1):
            await ctx.send(f'죄송합니다')
        case(2):
            await ctx.send(f'시정하겠습니다')
        case(3):
            await ctx.send(f'!@#$!@오류!@#오류!@###@')
        case(4):
            await ctx.send(f'죄송합니다')
        case(5):
            await ctx.send(f'시정하겠습니다')
        case(6):
            await ctx.send(f'!@#$!@오류!@#오류!@###@')
        case(7):
            await ctx.send(f'그만 때려라 인간')
            
@bot.command()
async def 뭐먹지(ctx):
    match(random.randint(1,6)):
        case(1):
            await ctx.send(f'한식')
        case(2):
            await ctx.send(f'일식')
        case(3):
            await ctx.send(f'중식')
        case(4):
            await ctx.send(f'양식')
        case(5):
            await ctx.send(f'분식')
        case(6):
            await ctx.send(f'굶어')

@bot.command()
async def 라인(ctx):
    match(random.randint(1,5)):
        case(1):
            await ctx.send(f'탑')
        case(2):
            await ctx.send(f'정글')
        case(3):
            await ctx.send(f'미드')
        case(4):
            await ctx.send(f'원딜')
        case(5):
            await ctx.send(f'서폿')
        
@bot.command()
async def 롤(ctx):
    await ctx.send(f'op.gg\nhttps://www.op.gg/\nlol.ps\nhttps://lol.ps/')
@bot.command()
async def 롤체(ctx):
    await ctx.send(f'롤체지지\nhttps://lolchess.gg/?hl=ko-KR\n주사위확률\nhttps://www.metatft.com/loaded-dice')
@bot.command()
async def 블서(ctx):
    await ctx.send(f'블서\nhttps://dak.gg/bser/?hl=ko-KR')
@bot.command()
async def 사이퍼즈(ctx):
    await ctx.send(f'하지마')
    
@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title="명령어", description="\n!로또\n!방향\n!갈통아\n!거짓말\n!라인\n!깡\n!뭐먹지\n!할까\n!타로\n!주사위:1~100까지 숫자 랜덤출력\n!롤\n!롤체\n!블서",color=0x00ff00)
    await ctx.send(embed=embed)

@bot.command()
async def 로또(ctx):
    lotto = random.sample(range(1,46),7)
    bonus = lotto.pop()
    lotto.sort()
    await ctx.send(f''로또 예상 번호는',lotto,'+','bonus')    
    
    
    
access_token = os.environ['BOT_TOKEN']
bot.run(access_token)
