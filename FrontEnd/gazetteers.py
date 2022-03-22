gazetteer_list = {
    'COU': ['ஆஸ்திரியா-ஹங்கேரி', 'பிரித்தானியா', 'ஓட்டோமான்', 'ஜெர்மன்', 'ரோமானியா', 'போலாந்து', 'அலுபேனியா',
            'பகரைன்', 'பெல்சியம்', 'எக்குவடோர்', 'எல் சால்வடோர்', 'ஸ்வாசிலாந்து', 'ஜோர்ஜியா', 'மெக்ஸிக்கோ',
            'செக்கோஸ்லோவேகியா', 'ஆப்கானிஸ்தான்', 'அல்பேனியா', 'அல்ஜீரியா', 'அன்டோரா', 'அங்கோலா',
            'ஆன்டிகுவா மற்றும் பார்புடா', 'அர்ஜென்டினா', 'ஆர்மீனியா', 'ஆஸ்திரேலியா', 'ஆஸ்திரியா', 'அஜர்பைஜான்',
            'பஹாமாஸ்', 'பஹ்ரைன்', 'பங்களாதேஷ்', 'பார்படாஸ்', 'பெல்ஜியம்', 'பூட்டான்', 'பொலிவியா', 'பிரேசில்',
            'புருனே', 'பல்கேரியா', 'புர்கினா பாசோ', 'கம்போடியா', 'கேமரூன்', 'கனடா', 'கேப் வெர்டே',
            'மத்திய ஆப்பிரிக்க குடியரசு', 'சாட்', 'சிலி', 'சீனா', 'கொலம்பியா', 'கொமரோஸ்', 'காங்கோ குடியரசு',
            'கோஸ்ட்டா ரிக்கா', 'குரோஷியா', 'கியூபா', 'சைப்ரஸ்', 'செ குடியரசு', 'டென்மார்க்', 'ஜிபூட்டி', 'டொமினிகா',
            'டொமினிக்கன் குடியரசு', 'ஈக்வடார்', 'எகிப்து', 'எல் சல்வடோர்', 'இங்கிலாந்து', 'எக்குவடோரியல் கினியா',
            'எரித்திரியா', 'எஸ்டோனியா', 'எத்தியோப்பியா', 'பால்க்லாந்து தீவுகள்', 'ஃபாரோ தீவுகள்', 'பிஜி', 'பின்லாந்து',
            'பிரான்ஸ்', 'மைக்ரோனேஷியா', 'பிரஞ்சு கயானா', 'பிரெஞ்சு பாலினேசியா', 'காபோன்', 'காம்பியா', 'ஜார்ஜியா',
            'ஜெர்மனி', 'கானா', 'ஜிப்ரால்டர்', 'கிரீஸ்', 'கிரீன்லாந்து', 'கிரெனடா', 'குவாம்', 'குவாடலூப்பே', 'குவாத்தமாலா',
            'குர்ன்சி', 'கினியா', 'கினியா-பிசாவ்', 'கயானா', 'ஹைட்டி', 'ஹோண்டுராஸ்', 'ஹாங்காங்', 'ஹங்கேரி',
            'ஹாலந்து', 'ஐஸ்லாந்து', 'இந்தியா', 'இந்தோனேசியா', 'ஈரான்', 'ஈராக்', 'அயர்லாந்து', 'இஸ்ரேல்', 'இத்தாலி',
            'ஐவரி கோஸ்ட்', 'ஜமைக்கா', 'ஜான் மாயன்', 'ஜப்பான்', 'ஜெர்சி', 'ஜோர்டான்', 'கஜகஸ்தான்', 'கென்யா',
            'கிரிபதி', 'கொசோவோ', 'குவைத்', 'கிர்கிஸ்தான்', 'லாவோஸ்', 'லாட்வியா', 'லெபனான்', 'லெசோதோ',
            'லைபீரியா', 'லிபியா', 'லிச்சென்ஸ்டீன்', 'லிதுவேனியா', 'லுஹான்ஸ்க் குடியரசு', 'லக்சம்பர்க்', 'மக்காவ்',
            'மாசிடோனியா', 'மடகாஸ்கர்', 'மலாவி', 'மலேசியா', 'மாலத்தீவுகள்', 'மாலி', 'மால்டா', 'மார்ஷல் தீவுகள்',
            'மார்டினிக்', 'மொரிட்டானியா', 'மொரிஷியஸ்', 'மயோட்டி', 'மெக்சிகோ', 'மால்டோவா', 'மொனாக்கோ',
            'மங்கோலியா', 'மொன்செராட்', 'மாண்டினீக்ரோ', 'மொராக்கோ', 'மொசாம்பிக்', 'மியான்மர்', 'நாகோர்னோ-கராபாக்',
            'நமீபியா', 'நவ்ரு', 'நேபாளம்', 'நெதர்லாந்து', 'புதிய கலிடோனியா', 'நியூசிலாந்து', 'நிகரகுவா', 'நைஜர்',
            'நைஜீரியா', 'நியு', 'நார்போக் தீவு', 'நார்போக் தீவு', 'வட கொரியா', 'வடக்கு சைப்ரஸ்', 'வடக்கு மரியானா தீவுகள்',
            'நார்வே', 'ஓமன்', 'பாகிஸ்தான்', 'பலாவ்', 'பாலஸ்தீனிய பிரதேசங்கள்', 'பனாமா', 'பப்புவா நியூ கினி',
            'பராகுவே', 'பெரு', 'பிலிப்பைன்ஸ்', 'பிட்காயின் தீவுகள்', 'போலந்து', 'போர்ச்சுகல்', 'பிரிட்னெஸ்ட்ரோவி',
            'போர்ட்டோ ரிக்கோ', 'கத்தார்', 'ருமேனியா', 'ரஷ்யா', 'ருவாண்டா', 'காங்கோ குடியரசு', 'சபா',
            'சஹ்ராவி குடியரசு', 'செயின்ட் பார்தெலமி', 'செயின்ட் ஹெலினா', 'செயின்ட் கிட்ஸ் மற்றும் நெவிஸ்', 'செயின்ட் லூசியா'
            'செயின்ட் மார்ட்டின்', 'செயிண்ட் பியர் மற்றும் மிக்குலோன்', 'செயின்ட் வின்சென்ட் மற்றும் கிரெனடைன்ஸ்',
            'சமோவா', 'சான் மரினோ', 'சாவோ டோம் மற்றும் பிரின்சிபி', 'சவூதி அரேபியா', 'ஸ்காட்லாந்து', 'சீலாண்ட்',
            'செனகல்', 'செர்பியா', 'சீஷெல்ஸ்', 'சியரா லியோன்', 'சிங்கப்பூர்', 'சிண்ட் யூஸ்டாஷியஸ்', 'சிண்ட் மார்டன்',
            'ஸ்லோவாக்கியா', 'ஸ்லோவேனியா', 'சாலமன் தீவுகள்', 'சோமாலியா', 'சோமாலிலாந்து', 'தென்னாப்பிரிக்கா',
            'தெற்கு ஜார்ஜியா மற்றும் தெற்கு சாண்ட்விச் தீவுகள்', 'தென் கொரியா', 'தெற்கு ஒசேஷியா', 'தெற்கு சூடான்',
            'ஸ்பெயின்', 'இலங்கை', 'சூடான்', 'சுரினாம்', 'ஸ்வால்பார்ட்', 'சுவாசிலாந்து', 'ஸ்வீடன்', 'சுவிட்சர்லாந்து',
            'சிரியா', 'தைவான்', 'தஜிகிஸ்தான்', 'தான்சானியா', 'தாய்லாந்து', 'திமோர்-லெஸ்டே', 'டோகெலாவ்',
            'டோங்கா', 'திபெத்', 'டிரினிடாட் மற்றும் டொபாகோ', 'டிரிஸ்டன் டா குன்ஹா', 'துனிசியா', 'துருக்கி',
            'துர்க்மெனிஸ்தான்', 'துருக்கியர்கள் மற்றும் கைகோஸ்', 'துவாலு', 'உகாண்டா', 'உக்ரைன்', 'ஐக்கிய அரபு நாடுகள்',
            'ஐக்கிய இராச்சியம்', 'ஐக்கிய அமெரிக்கா', 'உருகுவே', 'அமெரிக்க விர்ஜின் தீவுகள்', 'உஸ்பெகிஸ்தான்',
            'வனுவாடு', 'வாடிகன் நகரம்', 'வெனிசுலா', 'வியட்நாம்', 'மேற்கு சாஹாரா', 'ஏமன்', 'ஜாம்பியா',
            'ஜிம்பாப்வே'],

    'CITY': ['கொழும்பு', 'ஹிரோசிமா', 'மஞ்சூரியா', 'அல்சேஸ்', 'லொரையின்', 'பரிஸ்', 'ஷாங்காய்', 'பியூனஸ் அயர்ஸ்',
             'மும்பை', 'மெக்சிக்கோ நகரம்', 'கராச்சி', 'இஸ்தான்புல்', 'டெல்லி', 'மணிலா', 'மாஸ்கோ', 'டாக்கா',
             'சியோல்', 'ஸா பாலோ', 'லாகோஸ்', 'ஜகார்த்தா', 'டோக்கியோ', 'ஜூமடியன்', 'நியூயார்க்', 'தைபே',
             'கின்ஷாசா', 'லிமா', 'கெய்ரோ', 'லண்டன்', 'பெய்ஜிங்', 'தெஹ்ரான்', 'நான்சோங்', 'பொகோடா', 'ஹாங்காங்',
             'லாகூர்', 'ரியோ டி ஜெனிரோ', 'பாக்தாத்', 'தையன்', 'பாங்காக்', 'பெங்களூர்', 'யுவேயாங்', 'சாண்டியாகோ',
             'கைஃபெங்', 'கொல்கத்தா', 'டொராண்டோ', 'யாங்கோன்', 'சிட்னி', 'சென்னை', 'ரியாத்', 'வுஹான்',
             'செயிண்ட் பீட்டர்ஸ்பர்க்', 'சோங்கிங்', 'செங்டு', 'சிட்டகாங்', 'அலெக்ஸாண்டிரியா', 'லாஸ் ஏஞ்சல்ஸ்',
             'தியான்ஜின்', 'மெல்போர்ன்', 'அகமதாபாத்', 'பூசன்', 'அபிட்ஜான்', 'கானோ', 'ஹைதராபாத்', 'புயாங்',
             'யோகோஹாமா-ஷி', 'இபாதான்', 'சிங்கப்பூர்', 'அங்காரா', 'ஷென்யாங்', 'ஹோ சி மின் நகரம்', 'ஷியான்',
             'நகர முனை', 'பெர்லின்', 'மாண்ட்ரீல்', 'மாட்ரிட்', 'ஹார்பின்', 'சியான்', 'பியோங்யாங்', 'லான்ஜோவ்',
             'குவாங்சூ', 'காசாபிளாங்கா', 'டர்பன்', 'நான்ஜிங்', 'காபூல்', 'ஷென்சென்', 'கராகஸ்', 'புனே', 'சூரத்',
             'ஜித்தா', 'கான்பூர்', 'லுவாண்டா', 'அடிஸ் அபாபா', 'நைரோபி', 'தையுவான்', 'சால்வடார்', 'ஜெய்ப்பூர்',
             'தாருஸ் சலாம்', 'சிகாகோ', 'இன்சியான்', 'யுன்ஃபு', 'அல் பாஸ்ரா', 'ஓசகா-ஷி', 'மொகடிசு', 'டேகு', 'ரோம்',
             'சாங்சுன்', 'கியேவ்', 'டிரானா', 'அல்ஜியர்ஸ்', 'அன்டோரா லா வெல்லா', 'செயின்ட் ஜான்ஸ்', 'யெரெவன்',
             'கான்பெரா', 'வியன்னா', 'பாகு', 'டேன்ஜியர்', 'ஆர்கோஸ்', 'ஏதென்ஸ்', 'சானியா', 'தீப்ஸ்', 'நாஃப்லியோ',
             'லார்னாகா', 'திரிகால', 'கால்சிஸ்', 'லிஸ்பன்', 'காடிஸ்', 'பட்ராஸ்', 'சியோஸ்', 'நிகோசியா', 'ஜாதர்',
             'மைட்டிலீன்', 'யெரெவன்', 'செவில்லே', 'மலகா', 'மடினா', 'காக்லியாரி', 'மெசினா', 'டெர்பென்ட்', 'கோமோ',
             'ரோம்', 'ரெஜியோ டி கலாப்ரியா', 'பலேர்மோ', 'சைராகஸ்', 'வோல்டெரா', 'குரோடோன்', 'டரான்டோ', 'கோர்ஃபு',
             'கெர்கிரா', 'இஸ்தான்புல்', 'நேபிள்ஸ்', 'ஐபிசா', 'துரஸ்', 'சோசோபோல்', 'மார்சேய்', 'கவாலா', 'மாங்கலியா',
             'கான்ஸ்டன்டா', 'மாந்துவா', 'மிலன்', 'டைராஸ்', 'குடைசி', 'நெசெபார்', 'சான்ட் மார்டி டி எம்பரீஸ்', 'லாமியா',
             'செரஸ்', 'வெரியா', 'ரோட்ஸ்', 'ப்லோவ்டிவ்', 'பிடோலா', 'சோபியா', 'மெட்ஸ்', 'கபாலா', 'ஷ்கோத்ரா',
             'ஸ்டாரா ஜாகோரா', 'தெசலோனிகி', 'பெராட்', 'பார்சிலோனா', 'பெல்கிரேட்', 'நிஸ்', 'மேட்டரா', 'கார்டஜினா',
             'தரகோனா', 'பிராடிஸ்லாவா', 'வலென்சியா', 'ஸ்மெடெரெவோ', 'எவோரா', 'பாரிஸ்', 'சூரிச்', 'கொலோன்',
             'ட்ரையர்', 'லுகோ', 'கேசரெஸ்', 'மெரிடா', 'நிஜ்மேகன்', 'ஆக்ஸ்பர்க்', 'ஸ்கோப்ஜே', 'ஸ்ட்ராஸ்பேர்க்',
             'டோங்கரென்', 'திரிபோலி', 'அவலைட்ஸ்', 'அஸ்வான்', 'கான்ஸ்டன்டைன்', 'பெங்காசி', 'மென்டெஃபெரா',
             'அக்ஸும்', 'அலெக்ஸாண்டிரியா', 'மொகடிசு', 'கெய்ரோ', 'கிஸ்மயோ', 'ஃபெஸ்-அல்-பாலி', 'ஓஜ்தா', 'மராகேஷ்',
             'சான்சிபார்', 'பெனின் நகரம்', 'இஃபே', 'சோஃபாலா', 'பேட்', 'மொம்பாசா', 'மொரோனி', 'அகடெஸ்',
             'கானோ', 'திம்புக்டு', 'மலிந்தி', 'கான்பெரா', 'லெவுகா', 'ஆக்லாந்து', 'வெலிங்டன்', 'அடிலெய்டு',
             'கிங்ஸ்கோட்', 'மெல்போர்ன்', 'பெர்த்', 'அல்பானி', 'பிரிஸ்பேன்', 'ப்ளஃப்', 'கெரிக்கேரி', 'குலிமனே',
             'லாகோஸ்', 'ஓய்டா', 'கேப் டவுன்', 'குமாசி'],

    'PER': ['நிக்கோலாஸ் II', 'அலெக்சேய் புருசிலோவ்', 'ஜார்ஜஸ் கிளெமென்சியு', 'ஜோசப் ஜோப்ரே', 'பேர்டினண்ட் ஃபோக்',
               'ராபர்ட் நிவேலே', 'பிலிப் பெட்டேன்', 'ஹெர்பேர்ட் எச். அஸ்குயித்', 'டே. லாயிட் ஜார்ஜ்', 'டக்ளஸ் ஹேக்',
               'ஜான் ஜெலிக்கோ', 'விக்டர் இம்மானுவேல் III', 'லுய்கி கடோர்னா', 'ஆர்மண்டோ டயஸ்', 'வூட்ரோ வில்சன்',
               'ஜான் பேர்ஷிங்', 'வின்ஸ்டன் சர்ச்சில்', 'பிராங்க்ளின் டெலானோ ரூஸ்வெல்ட்', 'பேரரசர் ஹிரோஹிட்டோ',
               'அடோல்ஃப் ஹிட்லர்', 'பெனிட்டோ முசோலினி', 'ஜோசப் ஸ்டாலின்', 'டக்ளஸ் மாக்ஆர்தர்', 'டுவைட் ஐசனோவர்',
               'மன்னர் ஜார்ஜ் V', 'ஆபிரகாம் டெர்பி', 'ஜார்ஜ் ஸ்டீபென்சன்', 'நியூகாமன்', 'ஜான் கே', 'ஜேம்சு ஆர்கிரீவ்ஸ்',
                'ராபர்ட் புல்டன்', 'மைக்கேல் பாரடே', 'ஹென்றி கார்ட்', 'ஜான் பிரின்ட்லி', 'ஜேம்ஸ் வாட்', 'எலி விட்னி',
                'ரிச்சர்ட் ஆர்க்ரைட்'],

    'MON': ['ஜனவரி', 'பெப்ரவரி', 'மார்ச்', 'ஏப்ரல்', 'மே', 'ஜூனஂ', 'ஜூலை', 'ஆகஸஂடஂ', 'செப்டெம்பர்', 'அக்டோபர்',
              'நவம்பர்', 'டிசம்பர்'],

    'NORP': ['ஐரோப்பியர்', 'பிரித்தானியர்', 'செக்கொஸ்லோவேக்கியர்', 'ஜேர்மனியினர்', 'எகிப்தியர்', 'ரஷ்யர்', 'யூதர்',
             'ஒல்லாந்தர்'],

    'CONT': ['ஆசியா', 'ஆபிரிக்கா', 'வட அமெரிக்கா', 'தென் அமெரிக்கா', 'அன்டார்க்டிக்கா', 'ஐரோப்பா', 'ஆஸ்திரேலியா'],

    'KIN': ['தம்பபன்னி', 'உபதிஸ்ஸ நுவர', 'அனுராதபுரம்', 'பொலன்னறுவை', 'தம்பதெனிய', 'கம்பளை', 'கோட்டே',
            'சீதாவக்கை', 'கண்டி']
}

previous_word = {
    'ORDINAL': ['முதலாவது', 'இரண்டாவது', 'மூன்றாவது', 'நான்காவது', 'ஐந்தாவது', 'ஆறாவது', 'ஏழாவது', 'எட்டாவது',
                'ஒன்பதாவது', 'பத்தாவது', 'முதலாம்', 'இரண்டாம்', 'மூன்றாம்', 'நான்காம்', 'ஐந்தாம்',
                'ஆறாம்', 'ஏழாம்', 'எட்டாம்', 'ஒன்பதாம்', 'பத்தாம்', 'பதினொன்றாம்', 'பன்னிரண்டாம்', 'பதின்மூன்றாம்',
                'பதிநான்காம்', 'பதினைந்தாம்', 'பதினாறாம்', 'பதினேழாம்', 'பதினெட்டாம்', 'பத்தொன்பதாம்', 'இருபதாம்',
                'ஒரு', 'இரு'],
    'TER': ['வட', 'தென்', 'வடக்கு', 'கிழக்கு', 'தெற்கு', 'மேற்கு', 'வடகிழக்கு', 'வடமேற்கு', 'தென்மேற்கு', 'தென்கிழக்கு'],
    'COU': ['ஐக்கிய'],
    'ORG': ['சர்வதேச', 'தேசிய'],
    'TIME': ['கி.பி.', 'கி.மு.']
}

clue_words = {
    'ANT': ['கல்வெட்டு', 'சித்திரம்', 'சிற்பம்', 'சிற்பங்கள்', 'சித்திரங்கள்', 'சிலை', 'உருவம்', 'உருவங்கள்'],
    'EQUIP': ['கருவி', 'இயந்திரம்', 'என்ஜின்', 'உபகரணம்', 'ஆயுதம்', 'இயந்திரங்கள்', 'உபகரணங்கள் '],
    'CON': ['கொள்கை', 'முறை', 'சிந்தனை', 'எண்ணக்கரு'],
    'CUR': ['காசு', 'நாணயம்'],
    'GOD': ['பெருமான்', 'கடவுள்', 'பகவான்', 'தெய்வம்', 'குலதெய்வம்'],
    'IND': ['கைத்தொழில்'],
    'SEC': ['துறை'],
    'SKILL': ['கலை', 'அறிவு', 'கலையம்சம்', 'கலையம்சங்கள்'],
    'SOU': ['மூலாதாரம்', 'மூலாதாரங்கள்'],
    'SUB': ['பாடம்', 'பாடங்கள்'],
    'TAX': ['வரி', 'கட்டணம்'],
    'TER': ['பிரதேசம்', 'ஊர்', 'தீவு', 'குடியேற்றம்'],
    'WAT': ['ஆறு', 'கங்கை', 'நதி', 'சமுத்திரம்', 'கடல்', 'பெருங்கடல்', 'குளம்', 'வாவி', 'நீர்த்தேக்கம்', 'நீர்நிலை'],
    'LAN': ['மொழி'],
    'LAW': ['சட்டம்', 'சீர்த்திருத்தம்', 'சீர்த்திருத்தங்கள்', 'பிரகடனம்', 'கொள்கை', 'ஒப்பந்தம்'],
    'LIT': ['இலக்கியம்', 'காவியம்', 'காவியங்கள்', 'இலக்கியங்கள்', 'நூல்'],
    'LOC': ['மாளிகை', 'விகாரை', 'கோயில்', 'கோவில்', 'துறைமுகம்', 'பாராளுமன்றம்', 'முகாம்', 'சிறைச்சாலை'],
    'NAME': ['பெயர்'],
    'DES': ['பதவி'],
    'PRO': ['பொருள்' 'பொருட்கள்'],
    'REL': ['சமயம்'],
    'CITY': ['நகரம்', 'நகர்' 'தலைநகர்', 'தலைநகரம்'],
    'COU': ['நாடு'],
    'CONT': ['கண்டம்'],
    'PER': ['மன்னன்', 'மன்னர்', 'அரசன்', 'அரசர்', 'தலைவர்', 'ஜனாதிபதி', 'இராணுவ ஜெனரல்', 'இராணுவ வீரர்', 'தளபதி',
               'இளவரசன்', 'பேரரசன்', 'அமைச்சர்', 'பிரதமர்', 'சேனாதிபதி'],
    'ORG': ['திணைக்களம்', 'சங்கம்', 'அமைப்பு', 'சபை', 'ஆணைக்குழு', 'கம்பனி', 'குழு'],
    'YEAR': ['வருடம்', 'ஆண்டு', 'வருசம்', 'வருஷம்'],
    'MON': ['மாதம்', 'மாசம்'],
    'DATE': ['திகதி', 'நாள்', 'தேதி'],
    'TIME': ['நூற்றாண்டு', 'காலப்பகுதி', 'தொடக்கம்', 'முதல்', 'வரை', 'தசாப்தம்', 'இறுதிப்பகுதி', 'முன்னரைப்பகுதி',
             'நடுப்பகுதி', 'கி.பி.', 'கி.மு.'],
    'NUM': ['எண்ணிக்கை', 'பேர்'],
    'TRO': ['இராணுவம்', 'படை', 'படையினர்', 'இயக்கம்'],
    'EVE': ['மகாயுத்தம்', 'சம்பவம்', 'நிகழ்வு', 'போர்', 'யுத்தம்', 'சடங்கு', 'போராட்டம்', 'கிளர்ச்சி', 'புரட்சி'],
    'NORP': ['மக்கள்', 'வம்சத்தினர்', 'வம்சம்', 'வகுப்பினர்', 'இனத்தவர்', 'சமுதாயம்', 'சமுதாயத்தினர்'],
    'GOV': ['அரசு', 'கூட்டரசு', 'பேரரசு', 'வல்லரசு', 'கட்சி', 'ஆட்சி'],
    'KIN': ['இராச்சியம்', 'ராஜ்யம்', 'இராஜ்யம்', 'இராசதானி'],
    'FOOD': ['உணவு'],
    'COM': [],
    'FAC': []
}

multiple_named_entities = ['போன்ற', 'போன்றன', 'ஆகிய', 'ஆகியன', 'என்பன']

suffix = {
    'COU': ['லாந்து'],
    'NORP': ['அர்'],
    'CON': ['வாதம்'],
    'SUB': ['இயல்'],
    'WAT': ['வாவி'],
}

numbers = {
    'unit': ['ஒரு', 'இரு', 'ஒன்று', 'இரண்டு', 'மூன்று', 'நான்கு', 'ஐந்து', 'ஆறு', 'ஏழு', 'எட்டு', 'ஒன்பது', 'பத்து',
             'பதினொன்று', 'பன்னிரண்டு', 'பதின்மூன்று', 'பதினான்கு', 'பதினைந்து', 'பதினாறு', 'பதினேழு', 'பதினெட்டு',
             'பத்தொன்பது'],
    'tens': ['இருபது', 'இருபத்து', 'முப்பது', 'முப்பத்து', 'நாற்பது', 'நாற்பத்து', 'ஐம்பது', 'ஐம்பத்து', 'அறுபது', 'அறுபத்து',
             'எழுபது', 'எழுபத்து', 'எண்பது', 'எண்பத்து', 'தொண்ணூறு', 'தொண்ணூற்று'],
    'hundred': ['நூறு', 'இருநூறு', 'முன்னூறு', 'நானூறு', 'ஐநூறு', 'அறுநூறு', 'எழுநூறு', 'எண்ணூறு', 'தொள்ளாயிரம்',
                'நூற்று', 'இருநூற்று', 'முன்னூற்று', 'நானூற்று', 'ஐநூற்று', 'அறுநூற்று', 'எழுநூற்று', 'எண்ணூற்று',
                'தொள்ளாயிரத்து'],
    'thousand': ['ஆயிரம்', 'ஆயிரத்து', 'இரண்டாயிரம்', 'மூலாயிரம்', 'நான்காயிரம்', 'ஐயாயிரம்', 'ஆறாயிரம்', 'ஏழாயிரம்',
                 'எண்ணாயிரம்', 'ஒன்பதாயிரம்'],
    'scales': ['இலட்சம்', 'கோடி', 'மில்லியன்', 'பில்லியன்']
}