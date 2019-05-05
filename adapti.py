import webbrowser
import time
import getpass
import ctypes
import random
from selenium import webdriver

webpage =  r"https://aluno.usjt.br/SOL/aluno/index.php/index/seguranca/dev/instituicao/8"

print('R.A: ')
ra = input()
senha = getpass.getpass('Senha: ')

acertos = int(input("\nAcertos: "))
values = random.sample(range(0, 23), (24-acertos))
print(values)

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get(webpage)

rafield = driver.find_element_by_name("matricula")
rafield.send_keys(ra)
senhafield = driver.find_element_by_name("senha")
senhafield.send_keys(senha)

entrar = driver.find_element_by_name("logar")
entrar.click()

time.sleep(3)
driver.get("https://aluno.usjt.br/SOL/aluno/index.php/ead/ilang")
print('Waiting!!!')
xxx = input()

try:
	driver.switch_to.window(driver.window_handles[1])
except:
	driver.switch_to.window(driver.window_handles[0])

def lessons():

	for x in range(33):

		height = 0
		time.sleep(6)
		scrollHeight = driver.execute_script("return document.scrollingElement.scrollHeight; ")
		print(scrollHeight)

		while height < scrollHeight:

			height += 100
			time.sleep(0.02)
			driver.execute_script("window.scrollTo(0, "+str(height)+")") 
		
		time.sleep(2.5)
		proximabu = driver.find_element_by_xpath("//em[contains(text(), 'Próxima aula')]")
		proximabu.click()

	ctypes.windll.user32.MessageBoxW(0, "Atividade completa.", "Finalizado", 1)

def respbutton():
	time.sleep(0.8)
	respbu = driver.find_element_by_xpath("//em[contains(text(), 'RESPONDER')]")
	respbu.click()
	time.sleep(3)
	try:
		driver.switch_to.window(driver.window_handles[1])
	except:
		driver.switch_to.window(driver.window_handles[0])

	answers()

def answers():

	pagesource = driver.page_source

	if "Há algum tempo, venho estudando as piadas, com ênfase em sua constituição linguística. Por isso, embora a afirmação a seguir possa aparecer surpreendente, creio que posso garantir que se trata de uma verdade quase banal" in pagesource:
		
		if 8 in values:

			ans = driver.find_element_by_xpath("//label[contains(text(), 'sua função humorística.')]")
			ans.click()
			respbutton()

		else:

			ans = driver.find_element_by_xpath("//label[contains(text(), 'seu potencial como objeto de investigação.')]")
			ans.click()
			respbutton()

	else:

		if "O filme Menina de ouro conta a história de Maggie Fitzgerald, uma garçonete de 31 anos que vive sozinha em condições humildes e sonha em se tornar uma boxeadora profissional treinada por Frankie Dunn." in pagesource:
		
			if 9 in values:

				ans = driver.find_element_by_xpath("//label[contains(text(), 'naturalização de barreiras socioculturais responsáveis pela exclusão da mulher no boxe.')]")
				ans.click()
				respbutton()

			else:


				ans = driver.find_element_by_xpath("//label[contains(text(), 'transposição de limites impostos à mulher num espaço de predomínio masculino.')]")
				ans.click()
				respbutton()

		else: 

			if "É possível considerar as modalidades esportivas coletivas dentro de uma mesma lógica," in pagesource:

				if 10 in values:

					ans = driver.find_element_by_xpath("//label[contains(text(), 'proteção do próprio alvo.')]")
					ans.click()
					respbutton()

				else:

					ans = driver.find_element_by_xpath("//label[contains(text(), 'progressão da equipe.')]")
					ans.click()
					respbutton()

			else:

				if "Ó doce, ó longa, ó inexprimível melancolia dos jornais velhos! Conhece-se um homem diante de um deles. Pessoa que não sentir alguma coisa ao ler folhas de meio século, bem pode crer que não terá nunca uma das mais" in pagesource:

					if 11 in values:

						ans = driver.find_element_by_xpath("//label[contains(text(), 'objeto de devoção pessoal.')]")
						ans.click()
						respbutton()

					else:

						ans = driver.find_element_by_xpath("//label[contains(text(), 'instrumento de reconstrução da memória.')]")
						ans.click()
						respbutton()

				else:

					if "A London Eye é uma enorme roda-gigante na capital inglesa. Por ser um dos monumentos construídos para celebrar a entrada do terceiro milênio, ela também é conhecida como Roda do Milênio" in pagesource:

						if 12 in values:

							ans = driver.find_element_by_xpath("//label[contains(text(), '113')]")
							ans.click()
							respbutton()

						else:

							ans = driver.find_element_by_xpath("//label[contains(text(), '135')]")
							ans.click()
							respbutton()

					else:

						if "Uma cisterna de 6 000 L foi esvaziada em um período de 3 h. Na primeira hora foi utilizada apenas uma bomba, mas nas duas horas seguintes, a fim de reduzir o tempo de esvaziamento, outra bomba foi ligada junto com a primeira." in pagesource:

							if 13 in values:

								ans = driver.find_element_by_xpath("//label[contains(text(), '2500')]")
								ans.click()
								respbutton()

							else:

								ans = driver.find_element_by_xpath("//label[contains(text(), '1500')]")
								ans.click()
								respbutton()

						else:

							if 'O procedimento de perda rápida de "peso" é comum entre os atletas dos esportes de combate. Para participar de um torneio, quatro atletas da categoria até 66 kg' in pagesource:

								if 14 in values:

									ans = driver.find_element_by_xpath("//label[contains(text(), 'I e III')]")
									ans.click()
									respbutton()

								else:

									ans = driver.find_element_by_xpath("//label[contains(text(), 'II e III')]")
									ans.click()
									respbutton()

							else:

								if "Preocupada com seus resultados, uma empresa fez um balanço dos lucros obtidos nos últimos sete meses, conforme dados do quadro." in pagesource:

									if 15 in values:

										ans = driver.find_element_by_xpath("//label[contains(text(), 'VII')]")
										ans.click()
										respbutton()

									else:

										ctypes.windll.user32.MessageBoxW(0, "Por favor pressione V e somente depois aperte ok.", "Vai logo cacete", 1)
										respbutton()

								else:

									if "Uma pessoa comercializa picolés. No segundo dia de certo evento ela comprou 4 caixas de picolés, pagando R$ 16,00 a caixa com 20 picolés" in pagesource:

										if 16 in values:

											ans = driver.find_element_by_xpath("//label[contains(text(), 'R$ 0,96.')]")
											ans.click()
											respbutton()

										else:

											ans = driver.find_element_by_xpath("//label[contains(text(), 'R$ 1,40.')]")
											ans.click()											
											respbutton()

									else:

										if "O ábaco é um antigo instrumento de cálculo que usa notação posicional de base dez para representar números naturais. Ele pode ser apresentado em vários modelos" in pagesource:

											if 17 in values:

												ans = driver.find_element_by_xpath("//label[contains(text(), '46171')]")
												ans.click()												
												respbutton()

											else:

												ans = driver.find_element_by_xpath("//label[contains(text(), '460171')]")
												ans.click()												
												respbutton()

										else:		
										
											if "Para garantir a segurança de um grande evento público que terá início às 4 h da tarde, um organizador precisa monitorar a quantidade de pessoas presentes em cada instante. Para cada 2 000 pessoas se faz" in pagesource:

												if 18 in values:

													ans = driver.find_element_by_xpath("//label[contains(text(), '560')]")
													ans.click()													
													respbutton()

												else:

													ans = driver.find_element_by_xpath("//label[contains(text(), '860')]")
													ans.click()													
													respbutton()

											else:

												if "A permanência de um gerente em uma empresa está condicionada à sua produção no semestre. Essa produção é avaliada pela média do lucro mensal do semestre" in pagesource:

													if 19 in values:

														ans = driver.find_element_by_xpath("//label[contains(text(), '26')]")
														ans.click()														
														respbutton()

													else:

														ans = driver.find_element_by_xpath("//label[contains(text(), '35')]")
														ans.click()														
														respbutton()

												else:					

													if "Um dos grandes desafios do Brasil é o gerenciamento dos seus recursos naturais, sobretudo os recursos hídricos. Existe uma demanda crescente por água e o risco de racionamento não pode ser descartado" in pagesource:

														if 20 in values:

															ans = driver.find_element_by_xpath("//label[contains(text(), '3 meses e meio')]")
															ans.click()															
															respbutton()

														else:

															ans = driver.find_element_by_xpath("//label[contains(text(), '2 meses e meio')]")
															ans.click()															
															respbutton()

													else:					

														if "O cultivo de uma flor rara só é se do mês do plantio para o mês subsequente o clima da região possuir as seguintes pecul" in pagesource:

															if 21 in values:

																ans = driver.find_element_by_xpath("//label[contains(text(), 'dezembro')]")
																ans.click()
																
																respbutton()

															else:

																ans = driver.find_element_by_xpath("//label[contains(text(), 'janeiro')]")
																ans.click()																
																respbutton()

														else:					

															if "Um paciente necessita de reidratação endovenosa feita por meio de cinco frascos de soro durante 24 h. Cada frasco tem um volume de 800 mL de soro. Nas primeiras quatro horas" in pagesource:

																if 22 in values:

																	ans = driver.find_element_by_xpath("//label[contains(text(), '40')]")
																	ans.click()																	
																	respbutton()

																else:

																	ans = driver.find_element_by_xpath("//label[contains(text(), '24')]")
																	ans.click()																	
																	respbutton()

															else:					

																if "Um reservatório é abastecido com água por uma torneira e um ralo faz a drenagem da água desse reservatório. Os gráficos representam as vazões Q, em litro por minuto, do volume de água que entra no reservatório pela torneira" in pagesource:

																	if 23 in values:

																		ans = driver.find_element_by_xpath("//label[contains(text(), 'De 0 a 25')]")
																		ans.click()																		
																		respbutton()

																	else:

																		ans = driver.find_element_by_xpath("//label[contains(text(), 'De 5 a 10')]")
																		ans.click()
																		respbutton()

																else:					

																	answers2()
	return;

def answers2():

	pagesource = driver.page_source

	if "Ler não é decifrar, como num jogo de adivinhações, o sentido de um texto. É, a partir do texto, ser capaz de atribuir-lhe significado" in pagesource:

		if 0 in values:

			ans = driver.find_element_by_xpath("//label[contains(text(), 'Propor leituras diferentes das previsíveis.')]")
			ans.click()
			respbutton()

		else:

			ans = driver.find_element_by_xpath("//label[contains(text(), 'Discorrer sobre o ato de leitura')]")
			ans.click()			
			respbutton()

	else:

		if "O hoax, como é chamado qualquer boato ou farsa na internet, pode espalhar vírus entre os seus contatos. Falsos sorteios de celulares " in pagesource:

			if 1 in values:

				ans = driver.find_element_by_xpath("//label[contains(text(), 'desprezar mensagens que causem comoção.')]")
				ans.click()				
				respbutton()

			else:

				ans = driver.find_element_by_xpath("//label[contains(text(), 'analisar a linguagem utilizada nas mensagens')]")
				ans.click()				
				respbutton()

		else:

			if "Em casa, Hideo ainda podia seguir fiel ao imperador japonês e às tradições que trouxera no navio que aportara em Santos. […] Por isso Hideo exigia que, aos domingos, todos estivessem juntos" in pagesource:

				if 2 in values:

					ans = driver.find_element_by_xpath("//label[contains(text(), 'os conflitos de gênero tendem a ser neutralizados.')]")
					ans.click()					
					respbutton()

				else:

					ans = driver.find_element_by_xpath("//label[contains(text(), 'o lugar à mesa metaforiza uma estrutura de poder.')]")
					ans.click()					
					respbutton()

			else:

				if "Centro das atenções em um planeta cada vez mais interconectado, a Floresta Amazônica expõe inúmeros dilemas. Um dos mais candentes diz respeito à madeira e sua exploração econômica," in pagesource:

					if 3 in values:

						ans = driver.find_element_by_xpath("//label[contains(text(), 'noticiar as descobertas científicas oriundas da pesquisa.')]")
						ans.click()						
						respbutton()

					else:

						ans = driver.find_element_by_xpath("//label[contains(text(), 'apresentar informações e comentários sobre o livro.')]")
						ans.click()						
						respbutton()

				else:

					if "A origem da obra de arte (2002) é uma instalação seminal na obra de Marilá Dardot. Apresentada originalmente em sua primeira exposição individual" in pagesource:

						if 4 in values:

							ans = driver.find_element_by_xpath("//label[contains(text(), 'as letras-vaso são utilizadas para o plantio de mudas.')]")
							ans.click()							
							respbutton()

						else:

							ans = driver.find_element_by_xpath("//label[contains(text(), 'o observador da obra atua como seu criador.')]")
							ans.click()							
							respbutton()

					else:

						if "A poesia é marcada pela recriação do objeto por meio da linguagem, sem necessariamente explicá-lo. Nesse fragmento de João Cabral de Melo Neto, poeta da geração de 1945" in pagesource:

							if 5 in values:

								ans = driver.find_element_by_xpath("//label[contains(text(), 'uma máquina, levando em consideração a relevância do discurso técnico-científico pós-Revolução Industrial.')]")
								ans.click()								
								respbutton()

							else:

								ans = driver.find_element_by_xpath("//label[contains(text(), 'uma palavra, a partir de imagens com as quais ela pode ser comparada')]")
								ans.click()								
								respbutton()

						else:

							if "VERISSIMO, L. F." in pagesource:

								if 6 in values:

									ans = driver.find_element_by_xpath("//label[contains(text(), 'marcação temporal, evidenciada pela presença de palavras indicativas dos dias da semana.')]")
									ans.click()									
									respbutton()

								else:

									ans = driver.find_element_by_xpath("//label[contains(text(), 'tom humorístico, ocasionado pela ocorrência de palavras empregadas em contextos formais.')]")
									ans.click()									
									respbutton()

							else:

								if "GUTO MUNIZ. Disponível em 222.focoincena.com.br. Accesso em: 30 maio 2016." in pagesource:

									if 7 in values:

										ans = driver.find_element_by_xpath("//label[contains(text(), 'utilizar figurinos com adereços cômicos.')]")
										ans.click()										
										respbutton()

									else:

										ans = driver.find_element_by_xpath("//label[contains(text(), 'dispensar o edifício teatral para a sua realização.')]")
										ans.click()										
										respbutton()

								else:

									try:
										finalizadobu = driver.find_element_by_xpath("//em[contains(text(), 'CONCLUIR ATIVIDADE')]")
										finalizadobu.click()	
										ctypes.windll.user32.MessageBoxW(0, "Acabou o adapti. Obrigado.", "Finalizado", 1)
										time.sleep(2)
										ctypes.windll.user32.MessageBoxW(0, "Iremos iniciar a segunda parte, passar por todas as aulas.", "Segunda etapa", 1)
										lessons()
									except:
										time.sleep(2)
										ctypes.windll.user32.MessageBoxW(0, "Iremos iniciar a segunda parte, passar por todas as aulas.", "Segunda etapa", 1)
										lessons()

	return;

answers()