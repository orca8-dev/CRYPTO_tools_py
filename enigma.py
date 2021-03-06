from enigma.machine import EnigmaMachine

ROTORS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'Beta', 'Gamma']
REFLECTORS = ['B', 'C', 'B-Thin', 'C-Thin']

state = 'M4 UKW $ Gamma 2 4 $ 5 9 $ 14 3 $ 5 20 fv cd hu ik es op yl wq jm'
enc = 'zkrtwvvvnrkulxhoywoj'

rings = '4 9 3 20'
plug = 'fv cd hu ik es op yl wq jm'.upper()
pos = '2 5 14 5'
pos = ''.join(chr(int(x) - 1 + ord('A')) for x in pos.split())

for rf in REFLECTORS:
    for r2 in ROTORS:
        for r3 in ROTORS:
            for r4 in ROTORS:
                rotors = ['Gamma', r2, r3, r4]
                e = EnigmaMachine.from_key_sheet(rotors=rotors, ring_settings=rings, 
                    reflector=rf, plugboard_settings=plug)
                e.set_display(pos)
                txt = e.process_text(enc).lower()
                if 'csictf' in txt:
                    print(txt)
