import os

def limpar_tela():
    # Limpa o terminal no Windows ou Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

def rodar_quiz():
    limpar_tela()
    print("=" * 60)
    print("      QUIZ INTERATIVO: AUTOCUIDADO MENTAL NA ADOLESCÊNCIA     ")
    print("=" * 60)
    print("Responda com sinceridade para refletir sobre seus hábitos!\n")
    input("Pressione ENTER para começar...")

    perguntas = [
        {
            "id": 1,
            "pergunta": "Quando você se sente muito estressado ou sobrecarregado, qual costuma ser sua primeira reação?",
            "opcoes": [
                "A) Ficar em silêncio e me isolar no quarto.",
                "B) Desabafar com um amigo de confiança ou familiar.",
                "C) Passar horas jogando ou nas redes sociais para esquecer.",
                "D) Praticar um hobby, ouvir música ou fazer um esporte."
            ]
        },
        {
            "id": 2,
            "pergunta": "Quantas horas de sono você consegue dormir na maioria das noites?",
            "opcoes": [
                "A) Menos de 6 horas.",
                "B) Entre 6 e 7 horas.",
                "C) Entre 8 e 10 horas (o recomendado para sua idade!).",
                "D) Durmo muito no fim de semana, mas quase nada nos dias de aula."
            ]
        },
        {
            "id": 3,
            "pergunta": "Como é sua relação com as telas (celular/computador) antes de dormir?",
            "opcoes": [
                "A) Uso até o momento exato em que pego no sono.",
                "B) Tento desligar uns 30 minutos antes, mas nem sempre consigo.",
                "C) Desligo as telas pelo menos 1 hora antes para relaxar a mente.",
                "D) Acordo no meio da noite e fico checando as notificações."
            ]
        },
        {
            "id": 4,
            "pergunta": "Quando você comete um erro na escola ou em um jogo, o que você pensa?",
            "opcoes": [
                "A) 'Eu sou um fracasso, nunca faço nada certo'.",
                "B) 'Todo mundo vai rir de mim ou me julgar'.",
                "C) 'Erros acontecem, o que posso aprender com isso para a próxima?'.",
                "D) Ignoro o erro e finjo que nada aconteceu."
            ]
        },
        {
            "id": 5,
            "pergunta": "Como você reage quando percebe que seus amigos estão excluindo você ou agindo de forma estranha?",
            "opcoes": [
                "A) Tento mudar meu jeito de ser só para agradar e ser aceito.",
                "B) Converso abertamente com eles para entender o que está acontecendo.",
                "C) Fico triste e guardo tudo para mim, achando que o problema sou eu.",
                "D) Procuro focar em outras amizades que me fazem bem."
            ]
        },
        {
            "id": 6,
            "pergunta": "Com que frequência você tira um tempo na semana apenas para relaxar (sem obrigações ou telas)?",
            "opcoes": [
                "A) Nunca, sinto que estou sempre ocupado ou conectado.",
                "B) Raramente, só quando estou muito cansado.",
                "C) Às vezes, quando lembro de dar um tempo.",
                "D) Regularmente, organizo meu tempo para ter esse momento meu."
            ]
        },
        {
            "id": 7,
            "pergunta": "O que você faz quando percebe que uma rede social está te deixando para baixo ou com inveja?",
            "opcoes": [
                "A) Continuo rolando a tela, mesmo me sentindo mal.",
                "B) Silêncio ou dou 'unfollow' em contas que me fazem questionar meu valor.",
                "C) Deixo o celular de lado e vou fazer outra atividade offline.",
                "D) Tento postar algo perfeito para parecer que minha vida também é incrível."
            ]
        },
        {
            "id": 8,
            "pergunta": "Se um amigo estivesse passando por uma fase difícil e triste, o que você diria a ele?",
            "opcoes": [
                "A) 'Isso é drama, logo passa'.",
                "B) 'Estou aqui para o que precisar, quer conversar ou só companhia?'.",
                "C) 'Tenta não pensar nisso, vamos jogar algo para distrair'.",
                "D) Não saberia o que dizer e me afastaria por medo de piorar as coisas."
            ]
        },
        {
            "id": 9,
            "pergunta": "Você consegue identificar e dar nome às emoções que sente no dia a dia (ex: frustração, ansiedade, entusiasmo)?",
            "opcoes": [
                "A) Não, só sinto um aperto ou irritação e não sei explicar.",
                "B) Às vezes, mas a maioria das emoções me deixa confuso.",
                "C) Sim, consigo perceber o que engatilhou aquele sentimento.",
                "D) Prefiro ignorar o que sinto e seguir em frente."
            ]
        },
        {
            "id": 10,
            "pergunta": "Pedir ajuda profissional (como ir a um psicólogo) ou conversar com o conselheiro da escola significa o que para você?",
            "opcoes": [
                "A) Um sinal de fraqueza ou que a pessoa enlouqueceu.",
                "B) Um passo corajoso de autocuidado para entender melhor a si mesmo.",
                "C) Algo desnecessário que dá para resolver sozinho.",
                "D) Uma boa alternativa, mas teria vergonha de contar para os outros."
            ]
        }
    ]

    respostas_usuario = []

    for item in perguntas:
        limpar_tela()
        print(f"Pergunta {item['id']}/10:")
        print(f"\n{item['pergunta']}\n")
        for opcao in item['opcoes']:
            print(opcao)
        
        while True:
            resposta = input("\nSua resposta (A, B, C ou D): ").strip().upper()
            if resposta in ['A', 'B', 'C', 'D']:
                respostas_usuario.append(resposta)
                break
            else:
                print("Opção inválida! Digite apenas A, B, C ou D.")

    limpar_tela()
    print("=" * 60)
    print("                  QUIZ CONCLUÍDO COM SUCESSO!                 ")
    print("=" * 60)
    print("\nObrigado por responder! Lembre-se de que não existem respostas")
    print("certas ou erradas aqui, apenas caminhos de reflexão.\n")
    print("💡 Dica de Autocuidado:")
    print("Priorizar o seu sono, saber a hora de desconectar das telas")
    print("e conversar sobre seus sentimentos com adultos de confiança")
    print("são os pilares mais fortes para manter sua mente saudável.\n")
    print("=" * 60)

if __name__ == "__main__":
    rodar_quiz()