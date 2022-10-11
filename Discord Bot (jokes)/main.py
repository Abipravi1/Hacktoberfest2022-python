import discord
import random

client = discord.Client()
pave_words = ['natal', 'Natal', 'ano novo', 'Ano novo', 'Ano Novo', 'fim de ano', 'Fim de ano', 'Fim de Ano',
              'réveillon', 'Réveillon', 'John Nada', 'john nada', 'John', 'john', 'a praça é nossa', 'A praça é nossa']
philosophical_uncle = ['Afinal, é pavê ou pacomê?']

jokes_list = ['Se um dia você ficar trancado do lado de fora, converse com a fechadura, pois comunicação é a chave.',
              'Por que o jardineiro nunca briga com a planta? Porque ele sempre a rega.',
              'Como transformar um giz em uma cobra? É só colocar ele na água, pois o giz-boia.',
              'Se um vinho tinto se tornar um vinho branco ele morre na hora. Porque agora ele será EX-TINTO.',
              'Qual é a peça mais velha do carro? Se você respondeu vôlante, está errado. São os faraóis.',
              'Nara chegou tarde em casa e o jantar tinha acabado. Qual era a receita? Macarrão a-cabou-Nara.',
              'Por que Minas Gerais não tem praia? Porque quando o primeiro mineiro foi abençoar as terras, ele disse: livrai-nos do mar, amém.',
              'O que uma privada falou para outra? Nunca saberemos, a conversa era privada.',
              'Como faz pra ouvir muitas piadas? É só carregar um saco cheio de pintinhos.',
              'Como faz para bater recordes? É só colocar o livro do Guinness no liquidificador.',
              'Por que se deve pedir uma pessoa em namoro às 12:59? Porque uma hora ela aceita.',
              'Por que os químicos são ótimos em resolver problemas? Porque eles têm todas as soluções.',
              'Por que o técnico do time levou os jogadores para a piscina? Para treinar passes em profundidade.',
              'O tio do pavê não existe. Pavê não tem tio, tem acento circunflexo.',
              'Quem é a tia de um super-herói que trabalha como autônoma? A Tia MEI.',
              'O que o Batman tem no coração? Bat-mentos.',
              'Por que o padre só ama 1 pessoa? Porque ele tem um crush fixo.',
              'Por que o Brasil era mais cheiroso em 1500? Porque era uma colônia.',
              'Sabe porque colocaram um trampolim no polo norte? Pro urso polar.',
              'Qual é o idoso matemático que joga basquete? O pivô.',
              'O que acontece se um chinês se cortar? Xai Xang.',
              'Qual super-herói ataca os seus inimigos com as unhas? O homem arranha.',
              'O que a obra literária falou pro boleto? Eu conto ou você conta?',
              'Vocês viram o japonês que morreu? O Kimataro.',
              'Sabe por que a pele do matemático está vermelha? Porque ele tá cosseno.',
              'O que o cavalo disse ao desligar o telefone? Foi só um trote.',
              'Qual é o tênis preferido do psicólogo? Converse.',
              'Quais são as escolas mais saudáveis? As escolas integrais.',
              'O que uma abelha egoísta disse pra outra? Isso é mel!',
              'Como o padre bateu o carro da paróquia? Dando uma rezinha.',
              'Qual o nome da casa da ovelha? É a lan house.',
              'Por que a lua não quis mais comer? Porque ela estava cheia.',
              'Como as enzimas se reproduzem? Uma enzima da outra.',
              'Qual a comida que você só come se achar? Escondidinho.',
              'Vocês conhecem o site do cavalinho? O www ponto cavalinho ponto com ponto com ponto com ponto com...',
              'Qual o refrigerante favorito da galinha? Cócócóla.',
              'Já viu aquele telefone que fica no meio do mato? O telegrama.',
              'Por que o vampiro vai à sauna? Porque ele gosta de comida quente.',
              'Qual o animal que gostaria de ser um utensílio de cuidados pessoais? A ser-pente.',
              'Pra que se usa óculos verdes? Pra verde perto!',
              'Sabe como se come macarrão parafuso? Com chave de fenda.',
              'Qual presidente mais gostava de pintura e fotos emolduradas? Jânio Quadros.',
              'Em uma corrida de frutas a maçã está ganhando. O que acontece se ela diminuir? A uva passa.',
              'Como se chama o pai da Malu Mader? Malu Father.',
              'Como se chama a sorveteria do Michel Teló? Ice te pego.',
              'Se já é difícil matar dinossauros, Imagine Dragons.',
              'Qual o ditador que não era tão mau? O Napoleão Bom na parte.',
              'O que acontece quando o Jabuti entra em extinção? O jabuticaba.',
              'Qual elemento é mais forte do que o zinco? Zeis.',
              'Qual cidade brasileira com pior sistema de saúde? Sorocaba.',
              'Qual o tipo de cerveja dos vilões gaúchos? A cerveja puro mal, Tchê.',
              'Qual o cachorro que gosta de mergulhar? O pi tchibum.',
              'Qual o religioso que é capaz de parar um carro? O Frei Dimão.',
              'Qual é o inseto mais lento do mundo? A borbolenta.', 'Qual o pico mais gelado do mundo? O pico-lé.',
              'Qual o país com mais coisas velhas? Australha.', 'Onde os mentirosos vivem? Em Gana.',
              'Qual microorganismo que gosta de evangelizar? Salmo-Nela.',
              'Como as freiras secam as suas roupas? Convento.']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('!piada'):
        quote = jokes_list
        await message.channel.send(random.choice(quote))

    if any(word in msg for word in pave_words):
        await message.channel.send(random.choice(philosophical_uncle))


client.run('BOT ID')
