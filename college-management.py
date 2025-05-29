# Nome: Gabriel Munhoz de Paiva
# Curso: Análise e Desenvolvimento de Sistemas


import json

def menu_principal():
    print('')
    print('*****MENU PRINCIPAL*****')
    print('')
    print('(1) Gerenciar Estudantes.')
    print('(2) Gerenciar Disciplinas.')
    print('(3) Gerenciar Professores.')
    print('(4) Gerenciar Turmas.')
    print('(5) Gerenciar Matrículas.')
    print('(9) Sair.')
    print('')
    escolher_opcao = input('Escolha uma opção: ')
    return escolher_opcao

def selecionar_menu_principal():
    opcao = menu_principal()
    if opcao == '1':
        tipo_item = 'GERENCIAR ESTUDANTES'
    elif opcao == '2':
        tipo_item = 'GERENCIAR DISCIPLINAS'
    elif opcao == '3':
        tipo_item = 'GERENCIAR PROFESSORES'
    elif opcao == '4':
        tipo_item = 'GERENCIAR TURMAS'
    elif opcao == '5':
        tipo_item = 'GERENCIAR MATRÍCULAS'
    elif opcao == '9':
        tipo_item = 'SAIR'
    else:
        tipo_item = None
    if tipo_item:
        print(f'Você selecionou a opção "{tipo_item}".')
    return tipo_item

def menu_de_operacoes(tipo_item):
    print('')
    print(f'*****{tipo_item}*****')
    print('')
    print('(1) Incluir.')
    print('(2) Listar.')
    print('(3) Atualizar.')
    print('(4) Excluir.')
    print('(9) Voltar ao menu principal.')
    print('')
    return input('Escolha uma opção: ')

def selecionar_menu_operacoes(tipo_item):
    opcao_operacao = menu_de_operacoes(tipo_item)
    if opcao_operacao == '1':
        tipo_operacao = 'Incluir'
    elif opcao_operacao == '2':
        tipo_operacao = 'Listar'
    elif opcao_operacao == '3':
        tipo_operacao = 'Atualizar'
    elif opcao_operacao == '4':
        tipo_operacao = 'Excluir'
    elif opcao_operacao == '9':
        tipo_operacao = 'Voltar'
    else:
        tipo_operacao = None
    if tipo_operacao:
        print(f'Você selecionou a operação "{tipo_operacao}".')
    return tipo_operacao

def incluir_item_selecionado(listas, tipo_item):
    if tipo_item == 'GERENCIAR ESTUDANTES':
        while True:
            nome_estudante = input('Insira o nome do(a) estudante que deseja incluir: ')
            while True:
                try:
                    codigo_estudante = int(input('Insira o código do(a) estudante: '))
                    break
                except ValueError:
                    print('O código do(a) estudante tem que ser em números inteiros. Tente novamente.')
            codigo_existe = False
            for estudante in listas['estudante']:
                if estudante['Código'] == codigo_estudante:
                    print('Estudante já está cadastrado no sistema. Tente novamente.')
                    codigo_existe = True
                    break
            if not codigo_existe:
                cpf_estudante = input('Insira o CPF do(a) estudante: ')
                listas['estudante'].append({
                    'Nome do(a) estudante': nome_estudante,
                    'Código': codigo_estudante,
                    'CPF': cpf_estudante
                })
                salvar_arquivo(listas['estudante'], 'lista_estudantes.json')
                print('Estudante cadastrado(a) com sucesso!')
            adicionar_mais_estudante = input('Deseja adicionar mais algum(a) estudante? (s/n): ')
            if adicionar_mais_estudante == 'n':
                return
            elif adicionar_mais_estudante != 's':
                print('Resposta inválida. Tente novamente.')
                break

    elif tipo_item == 'GERENCIAR DISCIPLINAS':
        while True:
            nome_disciplina = input('Insira o nome da disciplina que deseja incluir: ')
            while True:
                try:
                    codigo_disciplina = int(input('Insira o código da disciplina: '))
                    break
                except ValueError:
                    print('O código da disciplina tem que ser em números inteiros. Tente novamente.')
            codigo_existe = False
            for disciplina in listas['disciplina']:
                if disciplina['Código'] == codigo_disciplina:
                    print('Disciplina já está cadastrada no sistema. Tente novamente.')
                    codigo_existe = True
                    break
            if not codigo_existe:
                listas['disciplina'].append({
                    'Nome da disciplina': nome_disciplina,
                    'Código': codigo_disciplina
                })
                salvar_arquivo(listas['disciplina'], 'lista_disciplinas.json')
                print('Disciplina cadastrada com sucesso!')
            adicionar_mais_disciplina = input('Deseja adicionar mais alguma disciplina? (s/n): ')
            if adicionar_mais_disciplina == 'n':
                return
            elif adicionar_mais_disciplina != 's':
                print('Resposta inválida. Tente novamente')
                break
    elif tipo_item == 'GERENCIAR PROFESSORES':
        while True:
            nome_prof = input('Insira o nome do(a) professor(a) que deseja incluir: ')
            while True:
                try:
                    codigo_prof = int(input('Insira o código do(a) professor(a): '))
                    break
                except ValueError:
                    print('O código do(a) professor(a) tem que ser em números inteiros. Tente novamente.')
            codigo_existe = False
            for professor in listas['professor']:
                if professor['Código'] == codigo_prof:
                    print('Professor(a) já está cadastrado(a) no sistema. Tente novamente.')
                    codigo_existe = True
                    break
            if not codigo_existe:
                cpf_prof = input('Insira o CPF do(a) estudante: ')
                listas['professor'].append({
                    'Nome do(a) professor(a)': nome_prof,
                    'Código': codigo_prof,
                    'CPF': cpf_prof
                })
                salvar_arquivo(listas['professor'], 'lista_professores.json')
                print('Professor(a) cadastrado(a) com sucesso!')
            adicionar_mais_prof = input('Deseja adicionar mais algum(a) professor(a)? (s/n): ')
            if adicionar_mais_prof == 'n':
                return
            elif adicionar_mais_prof != 's':
                print('Resposta inválida. Tente novamente.')
                break

    elif tipo_item == 'GERENCIAR TURMAS':
        while True:
            while True:
                try:
                    codigo_turma = int(input('Insira o novo código da turma que deseja incluir: '))
                    if any(turma['Código da turma'] == codigo_turma for turma in listas['turma']):
                        print('Uma turma com este código já está cadastrada. Tente novamente.')
                        continue
                    break
                except ValueError:
                    print('O código da turma tem que ser em número inteiro. Tente novamente.')
            while True:
                try:
                    codigo_prof = int(input('Insira o código do(a) professor(a) que pertencerá à essa turma: '))
                    break
                except ValueError:
                    print('O código do(a) professor(a) tem que ser em número inteiro. Tente novamente.')
            codigo_prof_existe = any(professor['Código'] == codigo_prof for professor in listas['professor'])
            if not codigo_prof_existe:
                print('Professor(a) não está cadastrado(a) em nosso sistema. Tente novamente.')
                continue
            while True:
                try:
                    codigo_disciplina = int(input('Insira o código da disciplina que pertencerá à essa turma: '))
                    break
                except ValueError:
                    print('O código da turma tem que ser em número inteiro. Tente novamente.')
            codigo_disciplina_existe = any(disciplina['Código'] == codigo_disciplina for disciplina in listas['disciplina'])
            if not codigo_disciplina_existe:
                print('Disciplina não está cadastrada em nosso sistema. Tente novamente.')
                continue
            listas['turma'].append({
                'Código da turma': codigo_turma,
                'Código do(a) professor(a)': codigo_prof,
                'Código da disciplina': codigo_disciplina
            })
            salvar_arquivo(listas['turma'], 'lista_turmas.json')
            print('Turma cadastrada com sucesso!')
            adicionar_mais_turma = input('Deseja adicionar mais alguma turma? (s/n): ')
            if adicionar_mais_turma == 'n':
                return
            elif adicionar_mais_turma != 's':
                print('Resposta inválida, tente novamente.')
                break

    elif tipo_item == 'GERENCIAR MATRÍCULAS':
        while True:
            try:
                codigo_turma = int(input('Insira o código da turma que deseja matricular o(a) estudante: '))
                codigo_estudante = int(input('Insira o código do(a) estudante que deseja matricular na turma: '))
                turma_existe = any(turma['Código da turma'] == codigo_turma for turma in listas['turma'])
                estudante_existe = any(estudante['Código'] == codigo_estudante for estudante in listas['estudante'])
                if turma_existe and estudante_existe:
                    matricula_existe = any(matricula['Código da turma'] == codigo_turma and matricula['Código do(a) estudante'] == codigo_estudante for matricula in listas['matricula'])
                    if matricula_existe:
                        print('O estudante já está matriculado(a) nesta turma.')
                    else:
                        listas['matricula'].append({
                            'Código da turma': codigo_turma,
                            'Código do(a) estudante': codigo_estudante
                        })
                        salvar_arquivo(listas['matricula'], 'lista_matriculas.json')
                        print('Matrícula salva com sucesso!')
                        while True:
                            adicionar_mais_matricula = input('Deseja adicionar mais alguma matrícula? (s/n): ')
                            if adicionar_mais_matricula == 'n':
                                return
                            elif adicionar_mais_matricula == 's':
                                break
                            else:
                                print('Resposta inválida, tente novamente.')
                else:
                    print('Código da turma ou do(a) estudante inválido.')
            except ValueError:
                print('Código da turma e código do(a) estudante precisam ser números inteiros. Tente novamente.')

def listar_item_selecionado(listas, tipo_item):
    if tipo_item == 'GERENCIAR ESTUDANTES':
        if not listas['estudante']:
            print('Não há estudantes cadastrados.')
        else:
            def get_nome(estudante):
                return estudante.get('Nome do(a) estudante')

            def get_codigo(estudante):
                return estudante.get('Código', None)
                
            def get_cpf(estudante):
                return estudante.get('CPF')

            lista_ordenada = sorted(listas['estudante'], key=get_codigo)
            print('Lista de estudantes:')
            for estudante in lista_ordenada:
                nome = get_nome(estudante)
                codigo = get_codigo(estudante)
                cpf = get_cpf(estudante)
                print(f"- {nome} (Código: {codigo}, CPF: {cpf})")
    

    elif tipo_item == 'GERENCIAR DISCIPLINAS':
        if not listas['disciplina']:
            print('Não há disciplinas cadastradas.')
        else:
            def get_nome(disciplina):
                return disciplina.get('Nome da disciplina')

            def get_codigo(disciplina):
                return disciplina.get('Código', None)

            lista_ordenada = sorted(listas['disciplina'], key=get_codigo)
            print('Lista de disciplinas:')
            for disciplina in lista_ordenada:
                nome = get_nome(disciplina)
                codigo = get_codigo(disciplina)
                print(f"- Disciplina: {nome} (Código: {codigo})")

    elif tipo_item == 'GERENCIAR PROFESSORES':
        if not listas['professor']:
            print('Não há professores cadastrados.')
        else:
            def get_nome(professor):
                return professor.get('Nome do(a) professor(a)')

            def get_codigo(professor):
                return professor.get('Código', None)
            
            def get_cpf(professor):
                return professor.get('CPF')

            lista_ordenada = sorted(listas['professor'], key=get_codigo)
            print('Lista de professores:')
            for professor in lista_ordenada:
                nome = get_nome(professor)
                codigo = get_codigo(professor)
                cpf = get_cpf(professor)

                print(f"- Professor: {nome} (Código: {codigo}, CPF: {cpf})")

    elif tipo_item == 'GERENCIAR TURMAS':
        if not listas['turma']:
            print('Não há turmas cadastradas.')
        else:
            def get_turma(turma):
                return turma.get('Código da turma')

            def get_professor(turma):
                return turma.get('Código do(a) professor(a)')
            
            def get_disciplina(turma):
                return turma.get('Código da disciplina')

            lista_ordenada = sorted(listas['turma'], key=get_turma)
            print('Lista de turmas:')
            for turmas in lista_ordenada:
                turma = get_turma(turmas)
                prof = get_professor(turmas)
                discip = get_disciplina(turmas)

                print(f"- Turma: {turma} (Professor(a): {prof}, Disciplina: {discip})")

    elif tipo_item == 'GERENCIAR MATRÍCULAS':
        if not listas['matricula']:
            print('Não há matrículas cadastradas.')
        else:
            def get_turma(matricula):
                return matricula.get('Código da turma')

            def get_estudante(matricula):
                return matricula.get('Código do(a) estudante')
            
            lista_ordenada = sorted(listas['matricula'], key=get_turma)
            print('Lista de Matrículas:')
            for matricula in lista_ordenada:
                turma = get_turma(matricula)
                aluno = get_estudante(matricula)
                print(f"- Turma: {turma} (Estudante: {aluno})")

def atualizar_item_selecionado(listas, tipo_item):
    if tipo_item == 'GERENCIAR ESTUDANTES':
        if listas['estudante'] == []:
            print('Não há estudantes cadastrados.')
        else:
            codigo_atual_estudante = input('Insira o código do(a) estudante que deseja atualizar: ')
            if not codigo_atual_estudante: 
                print('Você precisa inserir um código válido.')
                return
            try:
                codigo_atual_estudante = int(codigo_atual_estudante)
            except ValueError:
                print('O código do(a) estudante deve ser um número inteiro. Tente novamente.')
                return

            for estudante in listas['estudante']:
                if estudante['Código'] == codigo_atual_estudante:
                    print('Estudante encontrado(a)!')
                    print(f'Dados atuais: Nome: {estudante["Nome do(a) estudante"]}, Código: {estudante["Código"]}, CPF: {estudante["CPF"]}')                
                    novo_nome = input('Insira o novo nome do(a) estudante (pressione Enter para manter o atual): ')
                    novo_codigo = input('Insira o novo código do(a) estudante (pressione Enter para manter o atual): ')
                    novo_cpf = input('Insira o novo CPF do(a) estudante (pressione Enter para manter o atual): ')               
                    if novo_nome:
                        estudante['Nome do(a) estudante'] = novo_nome
                    if novo_codigo:
                        try:
                            estudante['Código'] = int(novo_codigo)
                        except ValueError:
                            print('O código do(a) estudante deve ser um número inteiro. Tente novamente.')
                            return
                    if novo_cpf:
                        professor['CPF'] = novo_cpf               
                    print('')
                    print('Dados do(a) estudante atualizados com sucesso!')
                    salvar_arquivo(listas['estudante'], 'lista_estudantes.json')
                    return

    elif tipo_item == 'GERENCIAR DISCIPLINAS':
        if listas['disciplina'] == []:
            print('Não há disciplinas cadastradas.')
        else:
            codigo_atual_disciplina = input('Insira o código da disciplina que deseja atualizar: ')
        
            if not codigo_atual_disciplina:  # Verifica se o usuário deixou o campo vazio
                print('Código inválido. Certifique-se de inserir um código válido.')
                return
        
            try:
                codigo_atual_disciplina = int(codigo_atual_disciplina)  # Converte para inteiro se não for vazio
            except ValueError:
                print('Erro: o código deve ser um número inteiro. Tente novamente.')
                return
        
            for disciplina in listas['disciplina']:
                if disciplina['Código'] == codigo_atual_disciplina:
                    print('Disciplina encontrada!')
                    print(f'Dados atuais: Nome: {disciplina["Nome da disciplina"]}, Código: {disciplina["Código"]}')
                
                    novo_nome = input('Insira o novo nome da disciplina (pressione Enter para manter o atual): ')
                    novo_codigo = input('Insira o novo código da disciplina (pressione Enter para manter o atual): ')
                
                # Verifica se o código foi preenchido antes de converter
                    if novo_codigo:
                        try:
                            novo_codigo = int(novo_codigo)
                        except ValueError:
                            print('Erro: o código deve ser um número inteiro. Tente novamente.')
                            return
                
                # Atualiza os dados da disciplina
                    if novo_nome:
                        disciplina['Nome da disciplina'] = novo_nome
                    if novo_codigo:
                        disciplina['Código'] = novo_codigo
                
                    print('')
                    print('Dados da disciplina atualizados com sucesso!')
                    salvar_arquivo(listas['disciplina'], 'lista_disciplinas.json')
                    return
        
            print('')
            print('Disciplina não encontrada.')
    elif tipo_item == 'GERENCIAR PROFESSORES':
        if listas['professor'] == []:
            print('Não há professores cadastrados.')
        else:
            codigo_atual_prof = input('Insira o código do(a) professor(a) que deseja atualizar: ')
            if not codigo_atual_prof: 
                print('Você precisa inserir um código válido.')
                return
            try:
                codigo_atual_prof = int(codigo_atual_prof)
            except ValueError:
                print('O código do(a) professor(a) deve ser um número inteiro. Tente novamente.')
                return

            for professor in listas['professor']:
                if professor['Código'] == codigo_atual_prof:
                    print('Professor(a) encontrado(a)!')
                    print(f'Dados atuais: Nome: {professor["Nome do(a) professor(a)"]}, Código: {professor["Código"]}, CPF: {professor["CPF"]}')                
                    novo_nome = input('Insira o novo nome do(a) professor(a) (pressione Enter para manter o atual): ')
                    novo_codigo = input('Insira o novo código do(a) professor(a) (pressione Enter para manter o atual): ')
                    novo_cpf = input('Insira o novo CPF do(a) professor(a) (pressione Enter para manter o atual): ')               
                    if novo_nome:
                        professor['Nome do(a) professor(a)'] = novo_nome
                    if novo_codigo:
                        try:
                            professor['Código'] = int(novo_codigo)
                        except ValueError:
                            print('O código do(a) professor(a) deve ser um número inteiro. Tente novamente.')
                            return
                    if novo_cpf:
                        professor['CPF'] = novo_cpf               
                    print('')
                    print('Dados do(a) professor(a) atualizados com sucesso!')
                    salvar_arquivo(listas['professor'], 'lista_professores.json')
                    return

        print('Professor(a) não encontrado(a).')

    elif tipo_item == 'GERENCIAR TURMAS':
        if listas['turma'] == []:
            print('Não há turmas cadastradas.')
        else:
            codigo_atual_turma = input('Insira o código da turma que deseja atualizar: ')
            if not codigo_atual_turma: 
                print('Você precisa inserir um código válido.')
                return
            try:
                codigo_atual_turma = int(codigo_atual_turma)
            except ValueError:
                print('O código da turma deve ser um número inteiro. Tente novamente.')
                return
            for turma in listas['turma']:
                if turma['Código da turma'] == codigo_atual_turma:
                    print('Turma encontrada!')
                    print(f'Dados atuais: Turma: {turma["Código da turma"]}, Professor(a): {turma["Código do(a) professor(a)"]}, Disciplina: {turma["Código da disciplina"]}')                
                    nova_turma = input('Insira o novo código da turma (pressione Enter para manter o atual): ')
                    if nova_turma:
                        try:
                            turma['Código da turma'] = int(nova_turma)
                        except ValueError:
                            print('O código da turma deve ser um número inteiro. Tente novamente.')
                            return
                    novo_prof = input('Insira o novo código do(a) professor(a) (pressione Enter para manter o atual): ')
                    if novo_prof:
                        try:
                            turma['Código do(a) professor(a)'] = int(novo_prof)
                        except ValueError:
                            print('O código do(a) professor(a) deve ser um número inteiro. Tente novamente.')
                            return
                    nova_disciplina = input('Insira o novo código da disciplina (pressione Enter para manter o atual): ')               
                    if nova_disciplina:
                        try:
                            turma['Código da disciplina'] = int(nova_disciplina)
                        except ValueError:
                            print('O código da disciplina deve ser um número inteiro. Tente novamente.')
                            return
                    print('')
                    print('Dados da turma atualizados com sucesso!')
                    salvar_arquivo(listas['turma'], 'lista_turmas.json')
                    return
            print('Turma não encontrada.')

    elif tipo_item == 'GERENCIAR MATRÍCULAS':
        if listas['matricula'] == []:
            print('Não há matrículas cadastradas.')
        else:
            codigo_atual_estudante = input('Insira o código do estudante que deseja atualizar na matrícula: ')
            if not codigo_atual_estudante: 
                print('Você precisa inserir um código válido.')
                return
            try:
                codigo_atual_estudante = int(codigo_atual_estudante)
            except ValueError:
                print('O código do estudante deve ser um número inteiro. Tente novamente.')
                return
            for matricula in listas['matricula']:
                if matricula['Código do(a) estudante'] == codigo_atual_estudante:
                    print('Estudante encontrado!')
                    print(f'Dados da matrícula: Turma: {matricula["Código da turma"]}, Estudante: {matricula["Código do(a) estudante"]}')                
                    nova_turma = input('Insira o novo código da turma para alterar na matrícula (pressione Enter para manter o atual): ')
                    if nova_turma:
                        try:
                            matricula['Código da turma'] = int(nova_turma)
                        except ValueError:
                            print('O código da turma deve ser um número inteiro. Tente novamente.')
                            return
                    novo_estudante = input('Insira o novo código do estudante para alterar na matrícula (pressione Enter para manter o atual): ')
                    if novo_estudante:
                        try:
                            matricula['Código do(a) estudante'] = int(novo_estudante)
                        except ValueError:
                            print('O código do(a) estudante deve ser um número inteiro. Tente novamente.')
                            return
                    print('')
                    print('Dados da turma atualizados com sucesso!')
                    salvar_arquivo(listas['matricula'], 'lista_matriculas.json')
                    return
            print('Matrícula não encontrada.')

def excluir_item_selecionado(listas, tipo_item):
    if tipo_item == 'GERENCIAR ESTUDANTES':
        if listas['estudante'] == []:
            print('Não há estudantes cadastrados.')
        else:
            try:
                codigo_estudante_excluir = int(input('Insira o código do(a) estudante que deseja excluir: '))
            except ValueError:
                print('Código inválido. Certifique-se de inserir um número inteiro.')
                return
            estudante_encontrado = False
            for estudante in listas['estudante']:
                if estudante['Código'] == codigo_estudante_excluir:
                    estudante_encontrado = True
                    confirmacao = input('Tem certeza que você deseja realizar essa ação? (s/n): ')
                    if confirmacao == 's':
                        listas['estudante'].remove(estudante)
                        print(f'O estudante {estudante["Nome do(a) estudante"]} de código {estudante["Código"]} foi excluído com sucesso!')
                        salvar_arquivo(listas['estudante'], 'lista_estudantes.json')
                        return
                    elif confirmacao == 'n':
                        print('Operação cancelada.')
                        return
                    else:
                        print('Comando incorreto. Tente novamente.')
                        return
            if not estudante_encontrado:
                print('Estudante não encontrado.')

    elif tipo_item == 'GERENCIAR DISCIPLINAS':
        if listas['disciplina'] == []:
            print('Não há disciplinas cadastradas.')
        else:
            try:
                codigo_disciplina_excluir = int(input('Insira o código da disciplina que deseja excluir: '))
            except ValueError:
                print('Código inválido. Certifique-se de inserir um número inteiro e tente novamente.')
                return
            disciplina_encontrada = False
            for disciplina in listas['disciplina']:
                if disciplina['Código'] == codigo_disciplina_excluir:
                    disciplina_encontrada = True 
                    confirmacao = input('Tem certeza que você deseja realizar essa ação? (s/n): ')           
                    if confirmacao == 's':
                        listas['disciplina'].remove(disciplina)
                        print(f'A disciplina {disciplina["Nome da disciplina"]} foi excluída com sucesso!')
                        salvar_arquivo(listas['disciplina'], 'lista_disciplinas.json')
                        return
                    elif confirmacao == 'n':
                        print('Operação cancelada.')
                        return
                    else:
                        print('Comando incorreto. Tente novamente.')
                        return
            if not disciplina_encontrada:
                print('Disciplina não encontrada.')

    elif tipo_item == 'GERENCIAR PROFESSORES':
        if listas['professor'] == []:
            print('Não há professores cadastrados.')
        else:
            try:
                codigo_prof_excluir = int(input('Insira o código do(a) professor(a) que deseja excluir: '))
            except ValueError:
                print('Código inválido. Certifique-se de inserir um número inteiro.')
                return
            prof_encontrado = False
            for professor in listas['professor']:
                if professor['Código'] == codigo_prof_excluir:
                    prof_encontrado = True
                    confirmacao = input('Tem certeza que você deseja realizar essa ação? (s/n): ')
                    if confirmacao == 's':
                        listas['professor'].remove(professor)
                        print(f'O(a) professor(a) {professor["Nome do(a) professor(a)"]} de código {professor["Código"]} foi excluído(a) com sucesso!')
                        salvar_arquivo(listas['professor'], 'lista_professores.json')
                        return
                    elif confirmacao == 'n':
                        print('Operação cancelada.')
                        return
                    else:
                        print('Comando incorreto. Tente novamente.')
                        return
            if not prof_encontrado:
                print('Professor não encontrado.')

    elif tipo_item == 'GERENCIAR TURMAS':
        if listas['turma'] == []:
            print('Não há turmas cadastradas.')
        else:
            try:
                codigo_turma_excluir = int(input('Insira o código da turma que deseja excluir: '))
            except ValueError:
                print('Código inválido. Certifique-se de inserir um número inteiro.')
                return
            turma_encontrada = False
            for turma in listas['turma']:
                if turma['Código da turma'] == codigo_turma_excluir:
                    turma_encontrada = True
                    confirmacao = input('Tem certeza que você deseja realizar essa ação? (s/n): ')
                    if confirmacao == 's':
                        listas['turma'].remove(turma)
                        print(f'A turma {turma["Código da turma"]} foi excluída com sucesso!')
                        salvar_arquivo(listas['turma'], 'lista_turmas.json')
                        return
                    elif confirmacao == 'n':
                        print('Operação cancelada.')
                        return
                    else:
                        print('Comando incorreto. Tente novamente.')
                        return
            if not turma_encontrada:
                print('Turma não encontrada.')
            if confirmacao == 'n':
                return            
            print('')
            print('Turma não encontrada.')

    elif tipo_item == 'GERENCIAR MATRÍCULAS':
        if listas['matricula'] == []:
            print('Não há matrículas cadastradas.')
        else:
            try:
                codigo_estudante_excluir = int(input('Insira o código do estudante que deseja excluir da matrícula: '))
            except ValueError:
                print('Código inválido. Certifique-se de inserir um número inteiro.')
                return
        
            estudante_encontrado = False
            for matricula in listas['matricula']:
                if matricula['Código do(a) estudante'] == codigo_estudante_excluir:
                    estudante_encontrado = True
                    confirmacao = input('Tem certeza que você deseja realizar essa ação? (s/n): ')
                    if confirmacao == 's':
                        listas['matricula'].remove(matricula)
                        print(f'O estudante de código {matricula["Código do(a) estudante"]} foi excluído com sucesso!')
                        salvar_arquivo(listas['matricula'], 'lista_matriculas.json')
                        return
                    elif confirmacao == 'n':
                        print('Operação cancelada.')
                        return
                    else:
                        print('Comando incorreto. Tente novamente.')
                        return
        
            if not estudante_encontrado:
                print('Matrícula não encontrada.')


def salvar_arquivo(listas, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(listas, arquivo, ensure_ascii=False)

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except:
        return []


listas = {
    'estudante': ler_arquivo('lista_estudantes.json'),
    'disciplina': ler_arquivo('lista_disciplinas.json'),
    'professor': ler_arquivo('lista_professores.json'),
    'turma': ler_arquivo('lista_turmas.json'),
    'matricula': ler_arquivo('lista_matriculas.json')
}

while True:
    tipo_item = selecionar_menu_principal()
    if tipo_item is None:
        print('Opção inválida. Tente novamente.')
    elif tipo_item == 'SAIR':
        print('Saindo do programa...')
        break
    if tipo_item:
        while True:
            tipo_operacao = selecionar_menu_operacoes(tipo_item)
            if tipo_operacao == 'Incluir':
                incluir_item_selecionado(listas, tipo_item)

            elif tipo_operacao == 'Listar':
                listar_item_selecionado(listas, tipo_item)

            elif tipo_operacao == 'Atualizar':
                atualizar_item_selecionado(listas, tipo_item)

            elif tipo_operacao == 'Excluir':
                excluir_item_selecionado(listas, tipo_item)

            elif tipo_operacao == 'Voltar':
                break
            else:
                print('Opção inválida. Tente novamente.')