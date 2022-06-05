import string
import streamlit as st

def LA(sentence):
  # init
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

  #string 'hoed'
  transition_table[('q36', 'h')] = 'q14'
  transition_table[('q0', 'h')] = 'q14'
  transition_table[('q14', 'o')] = 'q15'
  transition_table[('q15', 'e')] = 'q16'
  transition_table[('q16', 'd')] = 'q35'
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
    state = transition_table[(state, current_char)]
    if state == 'q35':
      st.write("kata saat ini: ", current, ', valid')
    if state == 'error':
      st.write('error in: ', current, "\n id: ", idx)
      break;
    idx = idx + 1

  if state == 'accept':
    st.write('semua kata di input: ', sentence, ', valid')
  
  return LA

# S -> NN VB NN
	# NN -> zij | hij | vlees | tofu | auto | hoed | schoen
  # VB -> eet | rijdt | gebruikt

st.write(""
#Vocabulary
Zij = she
hij = he
vlees = meat
tofu = tofu
auto = car
hoed = hat
schoen = shoe
eet = eat
rijdt = drives
gebruikt = use"")
         

sentence = st.text_input("Masukkan Kalimat Belanda: ")
button = st.button("Cek Kata")

if button:
  LA(sentence)
