def get_training_data():
    train_data = [[('1914', 'NUM', 'B-YEAR'), ('-', 'PUNCT', 'O'), ('1918', 'NUM', 'B-YEAR'), ('வரையிலான', 'ADP', 'O'), ('காலப்', 'NOUN', 'O'), ('பகுதியில்', 'NOUN', 'O'), ('உலகம்', 'NOUN', 'O'), ('முழுவதும்', 'ADV', 'O'), ('பரவிய', 'ADJ', 'O'), ('யுத்தம்', 'NOUN', 'B-EVE'), ('முதலாவது', 'ADJ', 'B-EVE'), ('உலக', 'NOUN', 'B_EVE'), ('மகாயுத்தம்', 'NOUN', 'I-EVE'), ('என', 'PART', 'O'), ('அழைக்கப்படுகின்றது', 'VERB', 'O')],
[('1870', 'NUM', 'B-YEAR'), ('இல்', 'ADP', 'O'), ('பிஸ்மார்க்', 'PROPN', 'B-PER'), ('ஐக்கிய', 'PROPN', 'B-COU'), ('ஜேர்மனியை', 'PROPN', 'I-COU'), ('உருவாக்கி', 'VERB', 'O'), ('அதனைப்', 'DET', 'O'), ('பலம்', 'ADJ', 'O'), ('வாய்ந்த', 'ADJ', 'O'), ('நாடாக்குவதற்காக', 'NOUN', 'O'), ('பிரான்சுடன்', 'PROPN', 'B-COU'), ('யுத்தத்தில்', 'NOUN', 'B-EVE'), ('ஈடுபட்டான்', 'VERB', 'O')],
[('1887இல்', 'NUM', 'B-YEAR'), ('ஜேர்மன்', 'PROPN', 'B-COU'), ('பேரரசனான', 'NOUN', 'O'), ('இரண்டாம்', 'ADJ', 'B-PER'), ('வில்லியம்', 'PROPN', 'B-PER'), ('ஜேர்மன்', 'PROPN', 'B-COU'), ('பிரதேசத்தோடு', 'NOUN', 'O'), ('மாத்திரம்', 'ADV', 'O'), ('திருப்தி', 'NOUN', 'O'), ('அடையவில்லை', 'VERB', 'O')],
[('ஜேர்மன்', 'PROPN', 'B-COU'), ('பேரரசு', 'NOUN', 'O'), ('ஒன்றை', 'NUM', 'O'), ('உருவாக்குவதற்காக', 'VERB', 'O'), ('ஜேர்மனி', 'PROPN', 'B-COU'), ('இராணுவத்தை', 'NOUN', 'O'), ('பலப்படுத்த', 'VERB', 'O'), ('பிஸ்மார்க்', 'PROPN', 'B-PER'), ('நடவடிக்கை', 'NOUN', 'O'), ('எடுத்தான்', 'VERB', 'O')],
[('ஆயுத', 'NOUN', 'O'), ('பலத்தால்', 'NOUN', 'O'), ('ஐந்து', 'NUM', 'B-NUM'), ('வருடங்களில்', 'NOUN', 'O'), ('பெற்றவைகளைப்', 'NOUN', 'O'), ('பாதுகாக்க', 'VERB', 'O'), ('மேலும்', 'DET', 'O'), ('50', 'NUM', 'B-NUM'), ('வருடங்கள்', 'NOUN', 'O'), ('ஆயுதம்', 'NOUN', 'O'), ('தரித்த', 'VERB', 'O'), ('நிலையில்', 'NOUN', 'O'), ('இருக்க', 'AUX', 'O'), ('வேண்டி', 'AUX', 'O'), ('வரும்', 'AUX', 'O'), ('என', 'PART', 'O'), ('ஜேர்மனிய', 'PROPN', 'O'), ('சேனாதிபதியாகிய', 'NOUN', 'O'), ('வொன்', 'PROPN', 'B-PER'), ('வோல்', 'PROPN', 'I-PER'), ('கே', 'PROPN', 'I-PER'), ('கூறியுள்ளார்', 'VERB', 'O')],
[('ஜேர்மனி', 'PROPN', 'B-COU'), ('உள்ளிட்ட', 'ADP', 'O'), ('நாடுகள்', 'NOUN', 'O'), ('மத்திய', 'ADJ', 'O'), ('ஜரோப்பிய', 'ADJ', 'O'), ('அணி', 'NOUN', 'O'), ('நாடுகள்', 'NOUN', 'O'), ('எனவும்', 'CONJ', 'O'), ('பிரான்ஸ்', 'PROPN', 'B-COU'), ('உள்ளிட்ட', 'CONJ', 'O'), ('நாடுகள்', 'NOUN', 'O'), ('நேச', 'NOUN', 'O'), ('நாடுகள்', 'NOUN', 'O'), ('எனவும்', 'CONJ', 'O'), ('அழைக்கப்பட்டன', 'VERB', 'O')],
[('ஆஸ்திரியாவின்', 'PROPN', 'B-COU'), ('முடிக்குரிய', 'ADJ', 'O'), ('இளவரசனாகிய', 'NOUN', 'O'), ('பிரான்சிஸ்', 'PROPN', 'B-PER'), ('பேர்டினன்ட்டும்', 'PROPN', 'B-PER'), ('அவரது', 'DET', 'O'), ('மனைவியும்', 'NOUN', 'O'), ('பொஸ்னியாவின்', 'PROPN', 'B-COU'), ('தலைநகராகிய', 'NOUN', 'O'), ('சரஜிவோ', 'PROPN', 'B-CITY'), ('நகரத்தில்', 'NOUN', 'O'), ('சுற்றுலா', 'NOUN', 'O'), ('மேற்கொண்டபோது', 'VERB', 'O'), ('கொலை', 'VERB', 'O'), ('செய்யப்பட்டார்கள்', 'VERB', 'O')],
[('ரஷ்யாவுக்கும்', 'PROPN', 'B-COU'), ('பிரான்சுக்கும்', 'PROPN', 'B-COU'), ('இடையில்', 'ADP', 'O'), ('நட்புறவு', 'NOUN', 'O'), ('நிலவியதால்', 'VERB', 'O'), ('ஜேர்மனி', 'PROPN', 'B-COU'), ('ரஷ்யாவைத்', 'PROPN', 'B-COU'), ('தாக்கும்போது', 'VERB', 'O'), ('பிரான்ஸ்', 'PROPN', 'B-COU'), ('ரஷ்யாவுக்கு', 'PROPN', 'B-COU'), ('உதவலாமென', 'VERB', 'O'), ('எண்ணிய', 'VERB', 'O'), ('ஜேர்மனி', 'PROPN', 'B-COU'), ('சற்றும்', 'ADV', 'O'), ('சிந்திக்காமல்', 'VERB', 'O'), ('பிரான்சுக்கெதிராக', 'PROPN', 'B-COU'), ('யுத்தப்', 'NOUN', 'O'), ('பிரகடனம்', 'NOUN', 'O'), ('செய்தது', 'VERB', 'O')],
[('ஜேர்மனி', 'PROPN', 'B-COU'), ('ஐக்கியமடைந்த', 'VERB', 'O'), ('காலம்', 'NOUN', 'O'), ('தொட்டு', 'ADP', 'O'), ('ஜேர்மனிக்கும்', 'PROPN', 'B-COU'), ('பிரான்சுக்கும்', 'PROPN', 'B-COU'), ('இடையில்', 'ADP', 'O'), ('கடுமையாக', 'ADV', 'O'), ('பகைமை', 'NOUN', 'O'), ('உணர்வு', 'VERB', 'O'), ('தொடர்ந்தன', 'VERB', 'O')],
[('பிரான்ஸ்', 'PROPN', 'B-COU'), ('யுத்தத்தில்', 'NOUN', 'O'), ('இறங்குவதற்கு', 'VERB', 'O'), ('முன்பாக', 'ADV', 'O'), ('அதனைத்', 'PRON', 'O'), ('தாக்குவதற்கு', 'VERB', 'O'), ('எண்ணிய', 'ADJ', 'O'), ('ஜேர்மனி', 'PROPN', 'O'), ('பெல்ஜியத்திற்குள்', 'PROPN', 'O'), ('புகுந்து', 'VERB', 'O'), ('பெல்ஜியம்', 'NOUN', 'O'), ('வழியாக', 'ADP', 'O'), ('பிரான்சைத்', 'NOUN', 'O'), ('தாக்க', 'VERB', 'O'), ('ஆரம்பித்தது', 'VERB', 'O')],
[('அமெரிக்கர்கள்', 'NOUN', 'B-GPE'), ('பயணம்', 'NOUN', 'O'), ('செய்த', 'VERB', 'O'), ('லூசிடானியா', 'PROPN', 'B-ART'), ('என்னும்', 'CONJ', 'O'), ('பயணிகள்', 'ADJ', 'O'), ('கப்பலொன்று', 'NOUN', 'O'), ('ஜேர்மனியின்', 'PROPN', 'B-COU'), ('நீர்மூழ்கிக்', 'NOUN', 'O'), ('கப்பலின்', 'NOUN', 'O'), ('மூலம்', 'ADP', 'O'), ('மூழ்கடிக்கப்பட்டமையால்', 'VERB', 'O'), ('ஐக்கிய', 'PROPN', 'B-COU'), ('அமெரிக்கா', 'PROPN', 'I-COU'), ('யுத்தத்தில்', 'NOUN', 'O'), ('இறங்கியது', 'VERB', 'O')],
[('நேசநாடுகள்', 'NOUN', 'B-ORG'), ('தொடர்ச்சியாக', 'ADV', 'O'), ('நடத்திய', 'VERB', 'O'), ('தாக்குதல்களின்', 'NOUN', 'O'), ('காரணமாக', 'ADP', 'O'), ('ஜேர்மனியின்', 'PROPN', 'B-COU'), ('படைப்', 'NOUN', 'O'), ('பலம்', 'NOUN', 'O'), ('ஒடுங்கியது', 'VERB', 'O')],
[('1914', 'NUM', 'B-YEAR'), ('முதல்', 'ADP', 'O'), ('1918', 'NUM', 'B-YEAR'), ('வரை', 'ADP', 'O'), ('நடந்த', 'VERB', 'O'), ('முதலாவது', 'ADJ', 'B-EVE'), ('உலக', 'NOUN', 'B-EVE'), ('மகாயுத்தம்', 'NOUN', 'B-EVE'), ('ஜேர்மனியின்', 'PROPN', 'B-COU'), ('தலைமையிலான', 'ADJ', 'O'), ('அச்சு', 'NOUN', 'B-ORG'), ('நாடுகளின்', 'NOUN', 'B-ORG'), ('தோல்வியுடன்', 'NOUN', 'O'), ('முடிவுக்கு', 'VERB', 'O'), ('வந்தது', 'VERB', 'O')],
[('முதலாவது', 'ADJ', 'B-EVE'), ('உலக', 'NOUN', 'B-EVE'), ('மகாயுத்தத்தின்', 'NOUN', 'B-EVE'), ('காரணமாக', 'ADP', 'O'), ('ஜேர்மன்', 'PROPN', 'B-COU'), ('பேரரசு,', 'NOUN', 'O'), ('ஆஸ்திரிய', 'PROPN', 'B-COU'), ('ஹங்கேரிப்', 'PROPN', 'I-COU'), ('பேரரசு,', 'NOUN', 'O'), ('துருக்கிப்', 'PROPN', 'B-COU'), ('பேரரசு', 'NOUN', 'O'), ('போன்ற', 'CONJ', 'O'), ('சர்வாதிகார', 'ADJ', 'O'), ('முடியாட்சிகள்', 'NOUN', 'O'), ('வீழ்ச்சியடைந்தன', 'VERB', 'O')],
[('யுத்த', 'NOUN', 'O'), ('முடிவில்', 'NOUN', 'O'), ('ஐக்கிய', 'PROPN', 'B-COU'), ('அமெரிக்காவும்', 'PRON', 'I-COU'), ('பிரித்தானியாவும்', 'PRON', 'B-COU'), ('உலக', 'NOUN', 'O'), ('வல்லரசுகள்', 'NOUN', 'O'), ('எனத்', 'PART', 'O'), ('தலை', 'VERB', 'O'), ('நிமிர்ந்தன', 'VERB', 'O')],
[('சர்வதேச', 'NOUN', 'B-ORG'), ('சங்கம்', 'NOUN', 'B-ORG'), ('உருவாகி', 'VERB', 'O'), ('20', 'NUM', 'B-NUM'), ('வருடகாலம்', 'NOUN', 'O'), ('போர்', 'NOUN', 'O'), ('நிகழாமல்', 'VERB', 'O'), ('தவிர்த்ததில்', 'VERB', 'O'), ('இச்சங்கம்', 'DET', 'O'), ('வெற்றி', 'NOUN', 'O'), ('கண்டது', 'VERB', 'O')],
[('இத்தாலி', 'PROPN', 'B-COU'), ('அபிசீனியாவை', 'PROPN', 'B-COU'), ('ஆக்கிரமித்தபோது', 'VERB', 'O'), ('இத்தாலிக்கு', 'PROPN', 'B-COU'), ('எதிராகப்', 'ADP', 'O'), ('பொருளாதாரத்', 'NOUN', 'O'), ('தடை', 'NOUN', 'O'), ('விதிக்கப்பட்டது', 'VERB', 'O')],
[('1989', 'NUM', 'B-YEAR'), ('செப்டெம்பர்', 'NOUN', 'B-MON'), ('மாதம்', 'NOUN', 'O'), ('முதல்', 'ADP', 'O'), ('1945', 'NUM', 'B-YEAR'), ('ஆகஸ்ட்', 'NOUN', 'B-MON'), ('வரை', 'ADP', 'O'), ('6', 'NUM', 'B-NUM'), ('வருடங்கள்', 'NOUN', 'O'), ('தொடர்ந்து', 'ADV', 'O'), ('உலகம்', 'NOUN', 'O'), ('முழுவதும்', 'ADV', 'O'), ('நடைபெற்ற', 'VERB', 'O'), ('இந்த', 'DET', 'O'), ('பயங்கரமான', 'ADJ', 'O'), ('யுத்தத்தை', 'NOUN', 'O'), ('இரண்டாம்', 'ADJ', 'B-EVE'), ('உலக', 'NOUN', 'B-EVE'), ('மகாயுத்தம்', 'NOUN', 'B-EVE'), ('என', 'PART', 'O'), ('அழைப்பர்', 'VERB', 'O')],
[('முதலாம்', 'ADJ', 'B-EVE'), ('உலக', 'NOUN', 'I-EVE'), ('மகாயுத்தத்தின்', 'NOUN', 'I-EVE'), ('பின்', 'PROPN', 'O'), ('மேற்குலக', 'NOUN', 'O'), ('நாடுகளின்', 'NOUN', 'O'), ('தலையீட்டால்', 'NOUN', 'O'), ('ஜேர்மனியில்', 'NOUN', 'B-COU'), ('புதிய', 'ADJ', 'O'), ('அரசொன்று', 'NOUN', 'O'), ('அமைக்கப்பட்டதோடு', 'NOUN', 'O'), ('அதனை', 'NOUN', 'O'), ('வைமார்', 'NOUN', 'B-ORG'), ('கூட்டரசு', 'NOUN', 'B-ORG'), ('என', 'PART', 'O'), ('அழைத்தனர்', 'VERB', 'O')],
[('1929', 'NUM', 'B-YEAR'), ('இல்', 'ADP', 'O'), ('உலகப்', 'NOUN', 'O'), ('பொருளாதார', 'PROPN', 'O'), ('நெருக்கடி', 'NOUN', 'O'), ('ஏற்பட்டபொழுது', 'VERB', 'O'), ('அது', 'DET', 'O'), ('ஜேர்மனியை', 'PROPN', 'B-COU'), ('மிக', 'ADV', 'O'), ('மோசமாகப்', 'ADV', 'O'), ('பாதிப்படையச்', 'VERB', 'O'), ('செய்தது', 'NOUN', 'O')],
[('அடோல்ப்', 'PROPN', 'B-PER'), ('ஹிட்லர்', 'PROPN', 'I-PER'), ('என்பவர்', 'AUX', 'O'), ('ஓர்', 'DET', 'O'), ('ஆஸ்திரியர்', 'NOUN', 'B-GPE')],
[('முதலாம்', 'ADJ', 'B-EVE'), ('உலக', 'NOUN', 'I-EVE'), ('மகாயுத்தத்தின்போது', 'NOUN', 'I-EVE'), ('அடோல்ப்', 'PROPN', 'B-PER'), ('ஹிட்லர்', 'PROPN', 'I-PER'), ('ஜேர்மனிக்காகப்', 'PROPN', 'B-COU'), ('போரிட்டார்', 'VERB', 'O')],
[('சிறை', 'NOUN', 'O'), ('வாழ்க்கையின்போது', 'NOUN', 'O'), ('ஹிட்லர்', 'PROPN', 'B-PER'), ('தனது', 'DET', 'O'), ('புகழ்பெற்ற', 'ADJ', 'O'), ('“எனது', 'NOUN', 'B-ART'), ('போராட்டம்”', 'NOUN', 'B-ART'), ('என்ற', 'PART', 'O'), ('நூலை', 'NOUN', 'O'), ('எழுதினார்', 'VERB', 'O')],
[('ஹிட்லரின்', 'PROPN', 'B-PER'), ('கட்சி', 'NOUN', 'O'), ('தேசிய', 'ADJ', 'B-ORG'), ('சோசலிசக்', 'NOUN', 'B-ORG'), ('கட்சி', 'NOUN', 'B-ORG'), ('என', 'PART', 'O'), ('அழைக்கப்பட்டது', 'VERB', 'O')],
[('ஹிட்லர்', 'PROPN', 'B-PER'), ('ஜேர்மனியின்', 'PROPN', 'B-COU'), ('சான்சலர்', 'NOUN', 'O'), ('பதவிக்கு', 'NOUN', 'O'), ('நியமிக்கப்படும்போது', 'VERB', 'O'), ('வொன்', 'PROPN', 'B-PER'), ('ஹின்டன்', 'PROPN', 'I-PER'), ('பர்க்', 'PROPN', 'I-PER'), ('என்பவர்', 'DET', 'O'), ('ஜேர்மனியின்', 'PROPN', 'B-COU'), ('ஜனாதிபதியாகப்', 'NOUN', 'O'), ('பதவி', 'NOUN', 'O'), ('வகித்தார்', 'VERB', 'O')],
[('1934', 'NUM', 'B-YEAR'), ('இல்', 'ADP', 'O'), ('சர்வதேச', 'NOUN', 'B-ORG'), ('சங்கத்தில்', 'NOUN', 'B-ORG'), ('இருந்து', 'ADP', 'O'), ('விலகிய', 'VERB', 'O'), ('ஹிட்லர்', 'PROPN', 'B-PER'), ('ஜேர்மனியை', 'PROPN', 'B-COU'), ('மீண்டும்', 'ADV', 'O'), ('யுத்தத்தை', 'NOUN', 'O'), ('நோக்கி', 'ADP', 'O'), ('இட்டுச்', 'VERB', 'O'), ('சென்றார்', 'VERB', 'O')],
[('1938', 'NUM', 'B-YEAR'), ('இல்', 'ADP', 'O'), ('அயல்', 'ADJ', 'O'), ('நாடாகிய', 'NOUN', 'O'), ('ஆஸ்திரியாவை', 'PROPN', 'B-COU'), ('ஆக்கிரமித்த', 'VERB', 'O'), ('ஹிட்லர்', 'PROPN', 'B-PER'), ('அதனை', 'DET', 'O'), ('ஜேர்மனியுடன்', 'PROPN', 'B-COU'), ('இணைத்துக்', 'VERB', 'O'), ('கொண்டு', 'CONJ', 'O'), ('அங்கு', 'DET', 'O'), ('நாசிசவாத', 'NOUN', 'O'), ('ஆட்சியொன்றை', 'NOUN', 'O'), ('ஆரம்பித்தார்', 'VERB', 'O')],
[('செக்கொஸ்சிலோவேக்கியா', 'PROPN', 'B-COU'), ('மீது', 'ADP', 'O'), ('தனது', 'DET', 'O'), ('அவதானத்தைச்', 'NOUN', 'O'), ('செலுத்திய', 'VERB', 'O'), ('ஹிட்லர்', 'PROPN', 'B-PER'), ('அங்கிருந்த', 'DET', 'O'), ('மக்களை', 'NOUN', 'O'), ('செக்கொஸ்லோவேக்கியர்', 'NOUN', 'B-GPE'), ('ஜேர்மனியினர்', 'NOUN', 'B-GPE'), ('என', 'PART', 'O'), ('அவர்களை', 'DET', 'O'), ('இனரீதியாகப்', 'NOUN', 'O'), ('பிரித்து', 'VERB', 'O'), ('சுடேட்டன்லாநீது', 'PROPN', 'B-COU'), ('என்னும்', 'CONJ', 'O'), ('பெயரில்', 'NOUN', 'O'), ('தனிநாடு', 'NOUN', 'O'), ('ஒன்றை', 'NUM', 'O'), ('உருவாக்க', 'VERB', 'O'), ('உதவினார்', 'VERB', 'O')],
[('செக்கொஸ்லோவேக்கியாவையும்', 'PROPN', 'B-COU'), ('ஆக்கிரமித்த', 'VERB', 'O'), ('ஹிட்லர்', 'PROPN', 'B-PER'), ('அந்நாட்டை', 'NOUN', 'O'), ('ஜேர்மனியின்', 'PROPN', 'B-COU'), ('ஆதிக்கத்தின்', 'NOUN', 'O'), ('கீழ்க்', 'ADP', 'O'), ('கொண்டு', 'VERB', 'O'), ('வந்தார்', 'VERB', 'O')],
[('ஹிட்லர்', 'PROPN', 'B-PER'), ('போலந்தை', 'PROPN', 'B-COU'), ('ஆக்கிரமித்ததோடு', 'VERB', 'O'), ('பிரித்தானியா,', 'PROPN', 'B-COU'), ('பிரான்ஸ்', 'PROPN', 'B-COU'), ('போன்ற', 'CONJ', 'O'), ('நாடுகள்', 'NOUN', 'O'), ('ஹிட்லருக்கு', 'PROPN', 'B-PER'), ('எதிராக', 'ADV', 'O'), ('யுத்தத்தை', 'NOUN', 'O'), ('ஆரம்பித்தன', 'VERB', 'O')],
[('1933', 'NUM', 'B-YEAR'), ('இல்', 'ADP', 'O'), ('ஆட்சிக்கு', 'NOUN', 'O'), ('வந்த', 'VERB', 'O'), ('ஹிட்லர்', 'PROPN', 'B-PER'), ('6', 'NUM', 'B-NUM'), ('வருடங்கள்', 'NOUN', 'O'), ('ஜேர்மனியைப்', 'PROPN', 'B-COU'), ('பலப்படுத்தி', 'VERB', 'O'), ('இரண்டாம்', 'ADJ', 'B-EVE'), ('உலக', 'NOUN', 'I-EVE'), ('மகா', 'ADJ', 'I-EVE'), ('யுத்தத்தை', 'NOUN', 'I-EVE'), ('ஆரம்பித்ததோடு', 'VERB', 'O'), ('ஹிட்லரைத்', 'PROPN', 'B-PER'), ('தோற்கடித்து', 'VERB', 'O'), ('ஜேர்மனியின்', 'PROPN', 'B-COU'), ('நாசிசவாதத்தை', 'NOUN', 'O'), ('உலகில்', 'NOUN', 'O'), ('இருந்து', 'ADP', 'O'), ('துடைத்தெறிய', 'VERB', 'O'), ('ஐக்கிய', 'PROPN', 'B-COU'), ('அமெரிக்கா,', 'PROPN', 'I-COU'), ('இங்கிலாந்து,', 'PROPN', 'B-COU'), ('ரஷ்யா', 'PROPN', 'B-COU'), ('உள்ளிட்ட', 'CONJ', 'O'), ('நட்பு', 'NOUN', 'O'), ('நாடுகளுக்கு', 'NOUN', 'O'), ('ஆறு', 'NUM', 'B-NUM'), ('வருடங்களாக', 'NOUN', 'O'), ('தொடர்ந்து', 'ADV', 'O'), ('ஹிட்லரோடு', 'PROPN', 'B-PER'), ('போராட', 'VERB', 'O'), ('வேண்டிய', 'AUX', 'O'), ('நிலை', 'NOUN', 'O'), ('ஏற்பட்டது', 'VERB', 'O')],
[('இக்காலகட்டத்தில்', 'NOUN', 'O'), ('ஹிட்லரால்', 'PROPN', 'B-PER'), ('வதை', 'NOUN', 'B-ART'), ('முகாம்கள்', 'NOUN', 'B-ART'), ('அமைக்கப்பட்டு', 'VERB', 'O'), ('அப்பாவி', 'ADJ', 'O'), ('யூதர்களும்', 'NOUN', 'B-GPE'), ('ரஷ்யர்களும்', 'NOUN', 'B-GPE'), ('இலட்சக்கணக்கில்', 'NOUN', 'O'), ('கொலை', 'NOUN', 'O'), ('செய்யப்பட்டனர்', 'VERB', 'O')],
[('முதலாம்', 'ADJ', 'B-EVE'), ('உலக', 'NOUN', 'I-EVE'), ('யுத்தத்தில்', 'NOUN', 'I-EVE'), ('இத்தாலி', 'PROPN', 'B-COU'), ('வெற்றி', 'NOUN', 'O'), ('பெற்ற', 'VERB', 'O'), ('அணியில்', 'NOUN', 'O'), ('இருந்தாலும்', 'ADV', 'O'), ('யுத்தத்தின்', 'NOUN', 'B-EVE'), ('பின்', 'ADP', 'O'), ('ஏற்படுத்திய', 'VERB', 'O'), ('சமாதான', 'NOUN', 'O'), ('ஒப்பந்தங்களின்படி', 'NOUN', 'O'), ('அந்நாட்டிற்குப்', 'NOUN', 'O'), ('பெரிதும்', 'ADV', 'O'), ('நன்மை', 'NOUN', 'O'), ('எதுவும்', 'ADV', 'O'), ('கிடைக்கவில்லை', 'VERB', 'O')],
[('இத்தாலியில்', 'PROPN', 'B-COU'), ('நிலவிய', 'VERB', 'O'), ('இத்தகைய', 'DET', 'O'), ('உறுதியற்ற', 'ADJ', 'O'), ('நிலையைத்', 'NOUN', 'O'), ('தனக்குச்', 'DET', 'O'), ('சாதகமாக்கிக்', 'ADV', 'O'), ('கொண்ட', 'VERB', 'O'), ('பெனிடோ', 'PROPN', 'B-PER'), ('முசோலினி', 'PROPN', 'B-PER'), ('1922', 'NUM', 'B-YEAR'), ('இல்', 'ADP', 'O'), ('பாசிசவாத', 'NOUN', 'B-ORG'), ('அரசியல்', 'NOUN', 'I-ORG'), ('கட்சி', 'NOUN', 'I-ORG'), ('ஊடாக', 'ADP', 'O'), ('இத்தாலியின்', 'PROPN', 'B-COU'), ('அரசியல்', 'NOUN', 'O'), ('அதிகாரத்தைக்', 'NOUN', 'O'), ('கைப்பற்றிக்', 'VERB', 'O'), ('கொண்டார்', 'AUX', 'O')],
[('முசோலினியின்', 'PROPN', 'B-PER'), ('அரசியல்', 'NOUN', 'O'), ('முறை', 'NOUN', 'O'), ('பாசிசவாதம்', 'NOUN', 'O'), ('என', 'PART', 'O'), ('அழைக்கப்படுகின்றது', 'VERB', 'O')],
[('1936', 'NUM', 'B-YEAR'), ('இல்', 'ADP', 'O'), ('முசோலினி', 'PROPN', 'B-PER'), ('ஆபிரிக்காவின்', 'PROPN', 'B-COU'), ('அபிசீனியாவைக்', 'PROPN', 'I-COU'), ('கைப்பற்றிக்', 'VERB', 'O'), ('கொண்டான்', 'VERB', 'O')],
[('19', 'NUM', 'B-TIME'), ('ஆம்', 'ADP', 'O'), ('நூற்றாண்டின்', 'NOUN', 'O'), ('இறுதி', 'ADJ', 'O'), ('அரைப்பகுதியில்', 'NOUN', 'O'), ('இருந்து', 'ADP', 'O'), ('ஆசிய', 'PROPN', 'O'), ('நாடுகளில்', 'NOUN', 'O'), ('ஜப்பான்', 'PROPN', 'B-COU'), ('முன்னேற்றகரமான', 'ADJ', 'O'), ('நாடாக', 'NOUN', 'O'), ('வளர்ச்சியடைந்தது', 'VERB', 'O')],
[('1934', 'NUM', 'B-YEAR'), ('இல்', 'ADP', 'O'), ('ஐப்பான்', 'PROPN', 'B-COU'), ('வட', 'ADJ', 'B-COU'), ('சீனாவில்', 'PROPN', 'I-COU'), ('மஞ்சூரியாவை', 'PROPN', 'B-CITY'), ('ஆக்கிரமித்து', 'VERB', 'O'), ('அதனைத்', 'DET', 'O'), ('தனது', 'DET', 'O'), ('ஆதிக்கத்தின்', 'NOUN', 'O'), ('கீழ்க்', 'ADP', 'O'), ('கொண்டு', 'VERB', 'O'), ('வந்தது', 'VERB', 'O')],
[('நட்பு', 'NOUN', 'O'), ('நாடுகள்', 'NOUN', 'O'), ('பிரித்தானியா,', 'PROPN', 'B-COU'), ('பிரான்ஸ்,', 'PROPN', 'B-COU'), ('ஐக்கிய', 'PROPN', 'B-COU'), ('அமெரிக்கா', 'PROPN', 'I-COU'), ('உள்ளிட்ட', 'CONJ', 'O'), ('மேற்கு', 'ADJ', 'O'), ('லிபரல்வாத', 'NOUN', 'O'), ('நாடுகள்', 'NOUN', 'O'), ('பல', 'DET', 'O'), ('இந்த', 'DET', 'O'), ('அணியில்', 'NOUN', 'O'), ('சேர்ந்தன', 'VERB', 'O')],
[('கம்யூனிச', 'ADJ', 'O'), ('ரஷ்யாவும்', 'NOUN', 'B-COU'), ('நட்பு', 'NOUN', 'B-TRO'), ('நாடுகள்', 'NOUN', 'B-TRO'), ('அணியைச்', 'NOUN', 'B-TRO'), ('சேர்ந்த', 'ADP', 'O'), ('ஒரு', 'DET', 'O'), ('நாடாகும்', 'NOUN', 'O')],
[('அச்சு', 'NOUN', 'B-TRO'), ('நாடுகளில்', 'NOUN', 'B-TRO'), ('ஜேர்மன்,', 'PROPN', 'B-COU'), ('இத்தாலி', 'PROPN', 'B-COU'), ('ஆகிய', 'CONJ', 'O'), ('ஐரோப்பிய', 'NOUN', 'O'), ('நாடுகள்', 'NOUN', 'O'), ('இரண்டும்', 'NUM', 'B-NUM'), ('1937', 'NUM', 'B-YEAR'), ('இல்', 'ADP', 'O'), ('ஜப்பானுடன்', 'PROPN', 'B-COU'), ('இரகசிய', 'ADJ', 'O'), ('ஒப்பந்தம்', 'NOUN', 'O'), ('ஒன்றைச்', 'NUM', 'O'), ('செய்தன', 'VERB', 'O')],
[('ஜேர்மனி', 'PROPN', 'B-COU'), ('கி.பி', 'AUX', 'B-TIME'), ('1939', 'NUM', 'B-YEAR'), ('செப்டெம்பர்', 'NOUN', 'B-MON'), ('முதலாந்', 'NUM', 'B-DATE'), ('திகதி', 'NOUN', 'O'), ('போலந்தை', 'PROPN', 'B-COU'), ('ஆக்கிரமித்ததோடு', 'VERB', 'O'), ('இரண்டாம்', 'ADJ', 'B-EVE'), ('உலக', 'NOUN', 'I-EVE'), ('யுத்தம்', 'NOUN', 'I-EVE'), ('ஆரம்பமாகியது', 'VERB', 'O')],
[('ஹிட்லர்', 'PROPN', 'B-PER'), ('நோர்வே,', 'PROPN', 'B-COU'), ('டென்மார்க்,', 'PROPN', 'B-COU'), ('ஒல்லாந்து,', 'PROPN', 'B-COU'), ('பெல்ஜியம்', 'PROPN', 'B-COU'), ('ஆகிய', 'CONJ', 'O'), ('நாடுகளைக்', 'NOUN', 'O'), ('கைப்பற்றினான்', 'VERB', 'O')],
[('1940', 'NUM', 'B-YEAR'), ('ஜுன்', 'NOUN', 'B-MON'), ('மாதத்தில்', 'NOUN', 'O'), ('பிரான்ஸைத்', 'PROPN', 'O'), ('தாக்கி', 'VERB', 'O'), ('அதன்', 'DET', 'O'), ('தலைநகர்', 'NOUN', 'O'), ('பரிஸ்', 'PROPN', 'B-CITY'), ('நகரைக்', 'NOUN', 'O'), ('கைப்பற்றினான்', 'VERB', 'O')],
[('சிறந்த', 'ADJ', 'O'), ('பேச்சாற்றலோடு', 'NOUN', 'O'), ('திறமையான', 'ADJ', 'O'), ('தலைவராகவும்', 'NOUN', 'O'), ('திகழ்ந்த', 'AUX', 'O'), ('சேர்ச்சில்', 'PROPN', 'B-PER'), ('ஒட்டுமொத்த', 'ADV', 'O'), ('பிரித்தானிய', 'NOUN', 'B-GPE'), ('மக்களையும்', 'NOUN', 'O'), ('நாசிகளுக்கெதிரான', 'NOUN', 'O'), ('போரில்', 'NOUN', 'O'), ('ஈடுபடுத்துவதில்', 'VERB', 'O'), ('வெற்றி', 'NOUN', 'O'), ('கண்டார்', 'VERB', 'O')],
[('1941', 'NUM', 'B-YEAR'), ('ஆம்', 'AUX', 'O'), ('ஆண்டு', 'NOUN', 'O'), ('நவம்பர்', 'NOUN', 'B-MON'), ('மாதம்', 'NOUN', 'O'), ('7', 'NUM', 'B-DATE'), ('ஆம்', 'AUX', 'O'), ('திகதி', 'NOUN', 'O'), ('ஐப்பான்', 'PROPN', 'B-COU'), ('பேர்ள்', 'PROPN', 'B-ART'), ('துறைமுகத்தின்', 'NOUN', 'O'), ('கடற்படை', 'NOUN', 'O'), ('முகாமைக்', 'NOUN', 'O'), ('குண்டு', 'NOUN', 'O'), ('வீசித்', 'VERB', 'O'), ('தாக்கியது', 'VERB', 'O')],
[('ஜப்பானுடன்', 'PROPN', 'B-COU'), ('இணைந்திருந்த', 'VERB', 'O'), ('ஜேர்மன்,', 'PROPN', 'B-COU'), ('இத்தாலி', 'PROPN', 'B-COU'), ('ஆகிய', 'CONJ', 'O'), ('நாடுகள்', 'NOUN', 'O'), ('அமெரிக்காவுக்கு', 'PROPN', 'B-COU'), ('எதிராக', 'ADV', 'O'), ('யுத்தப்', 'NOUN', 'O'), ('பிரகடனம்', 'VERB', 'O'), ('செய்தன', 'VERB', 'O')],
[('பிரான்சின்', 'PROPN', 'B-COU'), ('சக்கரவர்த்தியான', 'NOUN', 'O'), ('நெப்போலியன்', 'PROPN', 'B-PER'), ('பொனாபட்', 'PROPN', 'I-PER'), ('இதற்கு', 'DET', 'O'), ('முன்', 'ADP', 'O'), ('ரஷ்யாவை', 'PROPN', 'B-COU'), ('ஆக்கிரமிக்கச்', 'VERB', 'O'), ('சென்று', 'VERB', 'O'), ('படுதோல்வி', 'NOUN', 'O'), ('அடைந்து', 'VERB', 'O'), ('பல்லாயிரத்துக்கும்', 'NOUN', 'O'), ('அதிகமான', 'DET', 'O'), ('காயமடைந்த', 'ADJ', 'O'), ('வீரர்களுடன்', 'NOUN', 'O'), ('பின்வாங்கினான்', 'VERB', 'O')],
[('கி.பி', 'AUX', 'B-TIME'), ('1942', 'NUM', 'B-YEAR'), ('அளவில்', 'ADP', 'O'), ('இலங்கை,', 'PROPN', 'B-COU'), ('இந்தியா', 'PROPN', 'B-COU'), ('ஆகிய', 'CONJ', 'O'), ('நாடுகளைத்', 'NOUN', 'O'), ('தவிர', 'AUX', 'O'), ('முழு', 'ADJ', 'O'), ('தென்', 'NOUN', 'O'), ('மற்றும்', 'CONJ', 'O'), ('தென்கிழக்காசிய', 'NOUN', 'O'), ('நாடுகளையும்', 'NOUN', 'O'), ('ஐப்பான்', 'PROPN', 'B-COU'), ('கைப்பற்றியது', 'VERB', 'O')],
[('1945', 'NUM', 'B-YEAR'), ('மார்ச்', 'NOUN', 'B-MON'), ('மாதமளவில்', 'NOUN', 'O'), ('ஜேர்மனிக்கு', 'PROPN', 'B-COU'), ('வருகை', 'VERB', 'O'), ('தந்த', 'VERB', 'O'), ('நேச', 'NOUN', 'B-TRO'), ('நாடுகளின்', 'NOUN', 'I-TRO'), ('படைகள்', 'NOUN', 'I-TRO'), ('மே', 'NOUN', 'B-MON'), ('மாதமளவில்', 'NOUN', 'O'), ('பேர்ளின்', 'PROPN', 'B-CITY'), ('நகருக்குள்', 'NOUN', 'O'), ('பிரவேசித்தன', 'VERB', 'O')],
[('ஜப்பான்', 'PROPN', 'B-COU'), ('தனது', 'DET', 'O'), ('போர்ப்பலத்தை', 'NOUN', 'O'), ('நிரூபித்து', 'VERB', 'O'), ('சிங்கப்பூர்,', 'PROPN', 'B-COU'), ('மலேசியா,', 'PROPN', 'B-COU'), ('பர்மா,', 'PROPN', 'B-COU'), ('ஹொங்கொங்', 'PROPN', 'B-COU'), ('முதலிய', 'CONJ', 'O'), ('பிரித்தானியக்', 'PROPN', 'B-GPE'), ('குடியேற்ற', 'ADJ', 'O'), ('நாடுகளைக்', 'NOUN', 'O'), ('கைப்பற்றியது', 'VERB', 'O')],
[('1942', 'NUM', 'B-YEAR'), ('ஏப்பிரல்', 'NOUN', 'B-MON'), ('05', 'NUM', 'B-DATE'), ('ஆந்', 'PART', 'O'), ('திகதி', 'NOUN', 'O'), ('கொழும்புக்கும்', 'PROPN', 'B-CITY'), ('ஏப்பிரல்', 'NOUN', 'B-MON'), ('7', 'NUM', 'B-DATE'), ('ஆந்', 'PART', 'O'), ('திகதி', 'NOUN', 'O'), ('திருகோணமலைக்கும்', 'PROPN', 'B-CITY'), ('குண்டு', 'NOUN', 'O'), ('வீசப்பட்டன', 'VERB', 'O')],
[('எகிப்திய', 'ADJ', 'B-GPE'), ('மிசிர்', 'ADJ', 'I-GPE'), ('ஜனாதிபதி', 'NOUN', 'O'), ('அப்துல்', 'PROPN', 'B-PER'), ('கமால்', 'PROPN', 'I-PER'), ('நாசர்', 'PROPN', 'I-PER'), ('சமவுடைமைப்', 'NOUN', 'O'), ('பொருளாதார', 'PROPN', 'O'), ('முறையைப்', 'NOUN', 'O'), ('பின்பற்றி', 'VERB', 'O'), ('சுயஸ்', 'PROPN', 'B-ART'), ('கால்வாயை', 'NOUN', 'B-ART'), ('மக்கள்', 'NOUN', 'O'), ('மயப்படுத்தினார்', 'VERB', 'O')],
[('ஈராக்கினால்', 'PROPN', 'B-COU'), ('குவைட்', 'PROPN', 'B-COU'), ('ஆக்கிரமிக்கப்பட்டது', 'VERB', 'O')],
[('செயலாளர்', 'NOUN', 'O'), ('நாயகத்தின்', 'NOUN', 'O'), ('சிபாரிசின்படி', 'ADV', 'O'), ('நம்பிக்கைப்', 'NOUN', 'B-ORG'), ('பொறுப்புச்', 'NOUN', 'I-ORG'), ('சபையை', 'NOUN', 'I-ORG'), ('அகற்றுவதற்கு', 'VERB', 'O'), ('2005', 'NUM', 'B-YEAR'), ('இல்', 'ADP', 'O'), ('உலகத்', 'NOUN', 'B-EVE'), ('தலைவர்களின்', 'NOUN', 'I-EVE'), ('மகாநாடு', 'NOUN', 'I-EVE'), ('தீர்மானித்துள்ளது', 'VERB', 'O')],
[('1945', 'NUM', 'B-YEAR'), ('ஒக்டோபர்', 'NOUN', 'B-MON'), ('24', 'NUM', 'B-DATE'), ('ஆந்', 'PART', 'O'), ('திகதி', 'NOUN', 'O'), ('பிரகடனம்', 'NOUN', 'O'), ('உத்தியோக', 'ADV', 'O'), ('பூர்வமாக', 'ADV', 'O'), ('ஏற்றுக்', 'VERB', 'O'), ('கொள்ளப்பட்டு', 'VERB', 'O'), ('ஐக்கிய', 'NOUN', 'B-ORG'), ('நாடுகள்', 'NOUN', 'B-ORG'), ('சபை', 'NOUN', 'B-ORG'), ('உத்தியோக', 'ADV', 'O'), ('பூர்வமாக', 'ADV', 'O'), ('உதயமாகியது', 'VERB', 'O')],
[('கி.பி', 'AUX', 'B-TIME'), ('1945', 'NUM', 'B-YEAR'), ('ஆகஸ்ட்', 'NOUN', 'B-MON'), ('6', 'NUM', 'B-DATE'), ('ஹிரோசிமா', 'PROPN', 'B-CITY'), ('மீதும்', 'ADP', 'O'), ('ஆகஸ்ட்', 'NOUN', 'B-MON'), ('9', 'NUM', 'B-DATE'), ('ஆந்', 'PART', 'O'), ('திகதி', 'NOUN', 'O'), ('நாகசாக்கி', 'PROPN', 'B-CITY'), ('நகர்', 'NOUN', 'O'), ('மீதும்', 'ADP', 'O'), ('ஐக்கிய', 'PROPN', 'B-COU'), ('அமெரிக்காவினால்', 'PROPN', 'I-COU'), ('அணுகுண்டுகள்', 'NOUN', 'O'), ('வீசப்பட்டன', 'VERB', 'O')],
[('இரண்டாம்', 'ADJ', 'B-EVE'), ('உலக', 'NOUN', 'I-EVE'), ('யுத்தம்', 'NOUN', 'I-EVE'), ('நடைபெற்றுக்கொண்டிருக்கும்', 'VERB', 'O'), ('வேளையில்', 'ADP', 'O'), ('இடைநடுவில்', 'ADV', 'O'), ('பிரித்தானியப்', 'PROPN', 'B-GPE'), ('பிரதமர்', 'NOUN', 'O'), ('வின்ஸ்டன்', 'PROPN', 'B-PER'), ('சேர்ச்சில்', 'PROPN', 'I-PER'), ('மற்றும்', 'CONJ', 'O'), ('ஐக்கிய', 'PROPN', 'B-COU'), ('அமெரிக்க', 'PROPN', 'I-COU'), ('ஜனாதிபதி', 'NOUN', 'O'), ('பிராங்லின்', 'PROPN', 'B-PER'), ('ரூஸ்வெல்ட்', 'PROPN', 'I-PER'), ('1941', 'NUM', 'B-YEAR'), ('ஆகஸ்ட்', 'NOUN', 'B-MON'), ('மாதம்', 'NOUN', 'O'), ('அத்திலாந்திக்', 'NOUN', 'B-ART'), ('பிரகடனத்தில்', 'NOUN', 'O'), ('கையொப்பம்', 'NOUN', 'O'), ('இட்டனர்', 'VERB', 'O')],
[('1943', 'NUM', 'B-YEAR'), ('ஒக்டோபர்', 'NOUN', 'B-MON'), ('மாதம்', 'NOUN', 'O'), ('ரஷ்யா,', 'PROPN', 'B-COU'), ('பிரித்தானியா,', 'PROPN', 'B-COU'), ('ஐக்கிய', 'PROPN', 'B-COU'), ('அமெரிக்கா', 'PROPN', 'I-COU'), ('மற்றும்', 'CONJ', 'O'), ('சீனா', 'PROPN', 'B-COU'), ('ஆகிய', 'CONJ', 'O'), ('நாடுகளின்', 'NOUN', 'O'), ('வெளிவிவகார', 'NOUN', 'O'), ('அமைச்சர்கள்', 'NOUN', 'O'), ('மொஸ்கோ', 'PROPN', 'B-CITY'), ('நகரில்', 'NOUN', 'O'), ('நடைபெற்ற', 'VERB', 'O'), ('பேச்சுவார்த்தையில்', 'NOUN', 'O'), ('உலக', 'ADJ', 'O'), ('சமாதானத்தை', 'NOUN', 'O'), ('ஏற்படுத்துவதற்காகச்', 'VERB', 'O'), ('சர்வதேச', 'ADJ', 'O'), ('நாடுகளின்', 'NOUN', 'O'), ('அமைப்பொன்றை', 'NOUN', 'O'), ('அமைப்பது', 'VERB', 'O'), ('குறித்துக்', 'ADV', 'O'), ('கலந்துரையாடினர்', 'VERB', 'O')],
[('ஐக்கிய', 'NOUN', 'O'), ('நாடுகளின்', 'NOUN', 'O'), ('கொள்கைப்', 'NOUN', 'O'), ('பிரகடனத்தை', 'NOUN', 'O'), ('வடிவமைப்பதற்காக', 'VERB', 'O'), ('1945', 'NUM', 'B-YEAR'), ('ஜூன்', 'NOUN', 'B-MON'), ('மாதத்தில்', 'NOUN', 'O'), ('ஐக்கிய', 'PROPN', 'B-COU'), ('அமெரிக்காவின்', 'PROPN', 'I-COU'), ('சான்', 'PROPN', 'B-CITY'), ('பிரான்சிஸ்கோ', 'PROPN', 'I-CITY'), ('நகரில்', 'NOUN', 'O'), ('பேச்சுவார்த்தை', 'NOUN', 'O'), ('நடைபெற்றது', 'VERB', 'O')]]
    return train_data