import string
import streamlit as st

def LA(sentence):
  # init
  global state
  st.subheader("Lexical Analyzer")
  alphabet_list = list(string.ascii_lowercase)
  state_list = [
                'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 
                'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20',
                'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30',
                'q31', 'q32', 'q33', 'q34', 'q35', 'q36'
              ]
  transition_table = {}

  number_list = ['1','2','3','4','5','6','7','8','9','0']
  for state in state_list:
    for alphabet in alphabet_list:
      transition_table[(state, alphabet)] = 'error'
    for number in number_list:
      transition_table[(state, number)] = 'error'
    transition_table[(state, '#')] = 'error'
    transition_table[(state, ' ')] = 'error'

  # Deskripsi CFG untuk Bahasa Belanda
  # S -> NN VB NN
	# NN -> zij | hij | vlees | tofu | auto | hoed | schoen
  # VB -> eet | rijdt | gebruikt

  #state awal
  transition_table[("q0", " ")] = "q0"

  #state finish
  transition_table[("q35", "#")] = "accept"
  transition_table[("q35", " ")] = "q36"

  transition_table[('q36', '#')] = "accept"
  transition_table[('q36', ' ')] = 'q36'

  #string 'zij'
  transition_table[('q36', 'z')] = 'q1'
  transition_table[('q0', 'z')] = 'q1'
  transition_table[('q1', 'i')] = 'q2'
  transition_table[('q2', 'j')] = 'q35'
  transition_table[('q35', ' ')] = 'q36'

  #string 'hij'
  transition_table[('q36', 'h')] = 'q3'
  transition_table[('q0', 'h')] = 'q3'
  transition_table[('q3', 'i')] = 'q2'
  transition_table[('q2', 'j')] = 'q35'
  transition_table[('q35', ' ')] = 'q36'

  #string 'vlees'
  transition_table[('q36', 'v')] = 'q4'
  transition_table[('q0', 'v')] = 'q4'
  transition_table[('q4', 'l')] = 'q5'
  transition_table[('q5', 'e')] = 'q6'
  transition_table[('q6', 'e')] = 'q7'
  transition_table[('q7', 's')] = 'q35'
  transition_table[('q35', ' ')] = 'q36'

  #string 'tofu'
  transition_table[('q36', 't')] = 'q8'
  transition_table[('q0', 't')] = 'q8'
  transition_table[('q8', 'o')] = 'q9'
  transition_table[('q9', 'f')] = 'q10'
  transition_table[('q10', 'u')] = 'q35'
  transition_table[('q35', ' ')] = 'q36'

  #string 'auto'
  transition_table[('q36', 'a')] = 'q11'
  transition_table[('q0', 'a')] = 'q11'
  transition_table[('q11', 'u')] = 'q12'
  transition_table[('q12', 't')] = 'q13'
  transition_table[('q13', 'o')] = 'q35'
  transition_table[('q35', ' ')] = 'q36'

  #string 'boot'
  transition_table[('q36', 'b')] = 'q14'
  transition_table[('q0', 'b')] = 'q14'
  transition_table[('q14', 'o')] = 'q15'
  transition_table[('q15', 'o')] = 'q16'
  transition_table[('q16', 't')] = 'q35'
  transition_table[('q35', ' ')] = 'q36'

  #string 'schoen'
  transition_table[('q36', 's')] = 'q17'
  transition_table[('q0', 's')] = 'q17'
  transition_table[('q17', 'c')] = 'q18'
  transition_table[('q18', 'h')] = 'q19'
  transition_table[('q19', 'o')] = 'q20'
  transition_table[('q20', 'e')] = 'q21'
  transition_table[('q21', 'n')] = 'q35'
  transition_table[('q35', ' ')] = 'q36'

  #string 'eet'
  transition_table[('q36', 'e')] = 'q22'
  transition_table[('q0', 'e')] = 'q22'
  transition_table[('q22', 'e')] = 'q23'
  transition_table[('q23', 't')] = 'q35'
  transition_table[('q35', ' ')] = 'q36'

  #string 'rijdt'
  transition_table[('q36', 'r')] = 'q24'
  transition_table[('q0', 'r')] = 'q24'
  transition_table[('q24', 'i')] = 'q25'
  transition_table[('q25', 'j')] = 'q26'
  transition_table[('q26', 'd')] = 'q27'
  transition_table[('q27', 't')] = 'q35'
  transition_table[('q35', ' ')] = 'q36'

  #string 'gebruikt'
  transition_table[('q36', 'g')] = 'q28'
  transition_table[('q0', 'g')] = 'q28'
  transition_table[('q28', 'e')] = 'q29'
  transition_table[('q29', 'b')] = 'q30'
  transition_table[('q30', 'r')] = 'q31'
  transition_table[('q31', 'u')] = 'q32'
  transition_table[('q32', 'i')] = 'q33'
  transition_table[('q33', 'k')] = 'q34'
  transition_table[('q34', 't')] = 'q35'
  transition_table[('q35', ' ')] = 'q36'


  #Lexical Analysis
  idx = 0
  state = 'q0'
  current = ''
  input_string = sentence.lower() + "#"
  while state != 'accept':
    current_char = input_string[idx]
    current += current_char
    before_state = state
    state = transition_table[(state, current_char)]
    if state == 'q35':
      st.write(current, ' --> valid')
    if state == 'error':
      st.write('error in: ', current, "with the id of ", idx, 'and state of', before_state)
      break;
    idx = idx + 1

  if state == 'accept':
    st.write(sentence, '--> all valid')
  
  return LA

def Parser(sentence):
  st.subheader("Parser")
  tokens = sentence.lower().split()
  tokens.append('EOS')

  # definisi simbol
  non_terminals = ['S', 'NN', 'VB']
  terminals = ['zij', 'hij', 'vlees', 'tofu', 'auto', 'boot', 'schoen', 'eet', 'rijdt', 'gebruikt']

  parse_table = {}

  parse_table[('S', 'zij')] = ['NN', 'VB', 'NN']
  parse_table[('S', 'hij')] = ['NN', 'VB', 'NN']
  parse_table[('S', 'vlees')] = ['NN', 'VB', 'NN']
  parse_table[('S', 'tofu')] = ['NN', 'VB', 'NN']
  parse_table[('S', 'auto')] = ['NN', 'VB', 'NN']
  parse_table[('S', 'boot')] = ['NN', 'VB', 'NN']
  parse_table[('S', 'schoen')] = ['NN', 'VB', 'NN']
  parse_table[('S', 'eet')] = ['error']
  parse_table[('S', 'rijdt')] = ['error']
  parse_table[('S', 'gebruikt')] = ['error']
  parse_table[('S', 'EOS')] = ['error']

  parse_table[('NN', 'zij')] = ['zij']
  parse_table[('NN', 'hij')] = ['hij']
  parse_table[('NN', 'vlees')] = ['vlees']
  parse_table[('NN', 'tofu')] = ['tofu']
  parse_table[('NN', 'auto')] = ['auto']
  parse_table[('NN', 'boot')] = ['boot']
  parse_table[('NN', 'schoen')] = ['schoen']
  parse_table[('NN', 'eet')] = ['error']
  parse_table[('NN', 'rijdt')] = ['error']
  parse_table[('NN', 'gebruikt')] = ['error']
  parse_table[('NN', 'EOS')] = ['error']

  parse_table[('VB', 'zij')] = ['error']
  parse_table[('VB', 'hij')] = ['error']
  parse_table[('VB', 'vlees')] = ['error']
  parse_table[('VB', 'tofu')] = ['error']
  parse_table[('VB', 'auto')] = ['error']
  parse_table[('VB', 'boot')] = ['error']
  parse_table[('VB', 'schoen')] = ['error']
  parse_table[('VB', 'eet')] = ['eet']
  parse_table[('VB', 'rijdt')] = ['rijdt']
  parse_table[('VB', 'gebruikt')] = ['gebruikt']
  parse_table[('VB', 'EOS')] = ['error']

  # inisialisasi stack
  stack = []
  stack.append('#')
  stack.append('S')

  # inisialisasi input reading
  idx_token = 0
  symbol = tokens[idx_token]

  # proses table parse
  while (len(stack) > 0):
    top = stack[len(stack)-1]
    st.write('top = ', top)
    st.write('symbol  = ', symbol)
    if top in terminals:
      st.write('top adalah simbol terminal')
      if top == symbol:
        stack.pop()
        idx_token = idx_token + 1
        symbol = tokens[idx_token]
        if symbol == "EOS":
          stack.pop()
          st.write('isi stack:', stack)
      else:
        st.write('error')
        break
    elif top in non_terminals:
      st.write('top adalah simbol non-terminal')
      if parse_table[(top, symbol)][0] != 'error':
        stack.pop()
        symbol_to_be_pushed = parse_table[(top, symbol)]
        for i in range(len(symbol_to_be_pushed)-1,-1,-1):
          stack.append(symbol_to_be_pushed[i])
      else:
        st.write('error')
        break
    else:
      st.write('error')
      break
    st.write('isi stack: ', stack)
    st.write("-----------")

  # kesimpulan
  st.write()
  if symbol == 'EOS' and len(stack) == 0:
    st.write('Input string ', '"', sentence, '"', ' diterima, sesuai Grammar')
  else:
    st.write('Error, input string:', '"', sentence, '"', ', tidak diterima, tidak sesuai Grammar')
  
  return Parser


# S -> NN VB NN
# NN -> zij | hij | vlees | tofu | auto | boot | schoen
# VB -> eet | rijdt | gebruikt

st.title("DUTCH - Lexical Analyzer & Parser")

colSubjects, colVerbs, colObjects = st.columns(3)
with colSubjects:
	st.header("SUBJECTS")
	st.write("zij (she)")
	st.write("hij (he)")

with colVerbs:
	st.header("VERBS")
	st.write("eet (eat)")
	st.write("rijdt (drive)")
	st.write("gebruikt (use)")
	
with colObjects:
	st.header("OBJECTS")
	st.write("vlees (meat)")
	st.write("tofu (tofu)")
	st.write("auto (car)")
	st.write("boot (boat)")
	st.write("schoen (shoe)")

sentence = st.text_input("Masukkan Kalimat Belanda: ")
button = st.button("Cek Kata")

if button:
  LA(sentence)

  if state != 'error':
    st.write("")
    Parser(sentence)

  
