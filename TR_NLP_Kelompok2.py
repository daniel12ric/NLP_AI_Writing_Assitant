# Untuk RUN 
# streamlit run TR_NLP_Kelompok2.py

# Library yang perlu sebelum import
# pip install streamlit nltk language_tool_python textstat

import streamlit as st
import language_tool_python
from nltk.corpus import wordnet
import nltk
import re
import textstat

# ⛔ Hanya jika belum pernah download
# nltk.download('wordnet')
# nltk.download('omw-1.4')

# Inisialisasi grammar checker
tool = language_tool_python.LanguageTool('en-US', remote_server='https://api.languagetoolplus.com')

# Daftar kata umum dan saran akademik
common_words = {
    "good": ["beneficial", "positive", "advantageous"],
    "bad": ["harmful", "negative", "undesirable"],
    "things": ["aspects", "elements", "factors"],
    "stuff": ["materials", "items", "substances"],
    "a lot": ["many", "numerous", "a large number of"],
    "really": ["extremely", "highly", "very"],
    "big": ["significant", "major", "considerable"],
    "small": ["minor", "minimal", "limited"],
    "get": ["obtain", "receive", "acquire"],
    "make": ["create", "construct", "produce"],
    "show": ["demonstrate", "illustrate", "reveal"],
    "help": ["assist", "support", "facilitate"],
    "think": ["believe", "assume", "consider"],
    "say": ["state", "mention", "claim"],
    "need": ["require", "necessitate", "demand"],
    "use": ["utilize", "employ", "apply"],
    "deal with": ["address", "manage", "handle"],
    "put": ["place", "position", "insert"],
    "keep": ["maintain", "preserve", "retain"],
    "find out": ["discover", "identify", "determine"],
    "look at": ["examine", "analyze", "review"],
    "go up": ["increase", "rise", "escalate"],
    "go down": ["decrease", "decline", "drop"],
    "right now": ["currently", "at present", "at the moment"],
    "a lot of": ["numerous", "a great deal of", "a large number of"],
    "kind of": ["somewhat", "relatively", "moderately"],
    "very": ["highly", "extremely", "greatly"],
    "awesome": ["remarkable", "impressive", "outstanding"],
    "cool": ["interesting", "noteworthy", "unique"],
    "easy": ["simple", "straightforward", "uncomplicated"],
    "hard": ["difficult", "challenging", "demanding"],
    "like": ["such as", "for example", "similar to"],
    "also": ["in addition", "furthermore", "moreover"],
    "but": ["however", "nevertheless", "on the other hand"],
    "so": ["therefore", "thus", "as a result"],
    "maybe": ["perhaps", "possibly", "potentially"],
    "anyway": ["nonetheless", "regardless", "in any case"],
    "ok": ["acceptable", "satisfactory", "adequate"],
    "guy": ["individual", "person", "male"],
    "girl": ["female", "young woman", "student (contextual)"],
    "kids": ["children", "young learners", "youths"],
    "old": ["elderly", "aged", "senior"],
    "young": ["youthful", "juvenile", "early-aged"],
    "rich": ["wealthy", "affluent", "well-off"],
    "poor": ["underprivileged", "disadvantaged", "low-income"],
    "fast": ["rapid", "quick", "swift"],
    "slow": ["gradual", "delayed", "lethargic"],
    "easy to get": ["accessible", "readily available", "convenient"],
    "hard to get": ["limited", "scarce", "inaccessible"],
    "fix": ["repair", "resolve", "correct"],
    "break": ["damage", "destroy", "disrupt"],
    "job": ["occupation", "position", "profession"],
    "pay": ["compensate", "remunerate", "reward"],
    "boss": ["manager", "supervisor", "employer"],
    "start": ["initiate", "commence", "launch"],
    "end": ["conclude", "terminate", "complete"],
    "tell": ["inform", "notify", "report"],
    "ask": ["inquire", "request", "question"],
    "answer": ["respond", "reply", "address"],
    "happy": ["satisfied", "pleased", "content"],
    "sad": ["upset", "disappointed", "dissatisfied"],
    "mad": ["angry", "frustrated", "irritated"],
    "cool down": ["de-escalate", "calm", "moderate"],
    "think about": ["consider", "reflect on", "contemplate"],
    "give": ["provide", "offer", "deliver"],
    "show up": ["appear", "arrive", "attend"],
    "leave": ["depart", "exit", "withdraw"],
    "use again": ["reuse", "recycle", "repurpose"],
    "help out": ["assist", "support", "aid"],
    "fun": ["enjoyable", "entertaining", "amusing"],
    "boring": ["dull", "tedious", "uninteresting"],
    "tired": ["exhausted", "fatigued", "worn out"],
    "hungry": ["starving", "famished", "ravenous"],
    "scared": ["afraid", "frightened", "terrified"],
    "nice": ["pleasant", "lovely", "agreeable"],
    "mean": ["unkind", "harsh", "rude"],
    "smart": ["intelligent", "clever", "bright"],
    "dumb": ["unintelligent", "slow-witted", "ignorant"],
    "funny": ["humorous", "comical", "amusing"],
    "weird": ["strange", "odd", "unusual"],
    "hot": ["warm", "scorching", "sweltering"],
    "cold": ["chilly", "freezing", "icy"],
    "messy": ["disorganized", "untidy", "cluttered"],
    "clean": ["tidy", "neat", "spotless"],
    "friend": ["companion", "buddy", "peer"],
    "enemy": ["opponent", "rival", "adversary"],
    "important": ["essential", "vital", "critical"],
    "happy": ["joyful", "delighted", "thrilled"],
    "sad": ["gloomy", "sorrowful", "melancholic"],
    "got": ["obtained", "received", "acquired"],
    "getting": ["obtaining", "receiving", "acquiring"],
    "made": ["created", "produced", "constructed"],
    "making": ["creating", "producing", "constructing"],
    "putting": ["placing", "positioning", "inserting"],
    "kept": ["maintained", "preserved", "retained"],
    "keeps": ["maintains", "preserves", "retains"],
    "helps": ["assists", "supports", "facilitates"],
    "using": ["utilizing", "employing", "applying"],
    "used": ["utilized", "employed", "applied"],
    "shows": ["demonstrates", "illustrates", "reveals"],
    "said": ["stated", "claimed", "mentioned"],
    "says": ["states", "claims", "mentions"],
    "needs": ["requires", "demands", "necessitates"],
    "looks": ["appears", "seems", "resembles"],
    "asks": ["inquires", "requests", "questions"],
    "asks for": ["requests", "seeks", "demands"],
    "wants": ["desires", "wishes", "intends"],
    "wanted": ["desired", "intended", "hoped for"],
    "trying": ["attempting", "endeavoring", "seeking to"],
    "try": ["attempt", "endeavor", "make an effort to"],
    "goes up": ["increases", "rises", "escalates"],
    "went down": ["decreased", "declined", "dropped"],
    "comes from": ["originates from", "derives from", "emerges from"],
    "okay": ["acceptable", "satisfactory", "adequate"],
    "bad thing": ["negative aspect", "drawback", "disadvantage"],
    "good thing": ["positive aspect", "benefit", "advantage"],
    "thing is": ["the issue is", "the main point is"],
    "pretty": ["relatively", "fairly", "somewhat"],
    "cool": ["interesting", "noteworthy", "unique"],
    "fun": ["enjoyable", "entertaining", "amusing"],
    "boring": ["dull", "tedious", "unengaging"],
    "awesome": ["excellent", "impressive", "remarkable"],
    "super": ["extremely", "very", "highly"],
    "really good": ["excellent", "outstanding", "notable"],
    "not good": ["unfavorable", "problematic", "ineffective"],
    "bad at": ["ineffective in", "lacking skill in", "unskilled in"],
    "good at": ["proficient in", "skilled at", "competent in"],
    "waste of time": ["inefficient", "unproductive", "time-consuming"],
    "thing to do": ["action", "activity", "approach"],
    "do stuff": ["perform tasks", "carry out activities", "complete work"],
    "go to": ["attend", "visit", "participate in"],
    "hang out": ["spend time", "socialize", "gather"],
    "come back": ["return", "reappear", "resume"]
}


style_patterns = {
    "i think": "It is believed that",
    "a lot of people": "Many individuals",
    "in my opinion": "It can be argued that",
    "kids": "children",
    "gonna": "going to",
    "wanna": "want to",
    "a lot of": "a large number of",
    "really big": "significant",
    "really important": "crucial",
    "kind of": "somewhat",
    "sort of": "to some extent",
    "stuff": "materials",
    "things": "aspects",
    "get": "obtain",
    "make sure": "ensure",
    "give": "provide",
    "put": "place",
    "deal with": "address",
    "come up with": "develop",
    "talk about": "discuss",
    "look at": "examine",
    "find out": "discover",
    "go up": "increase",
    "go down": "decrease",
    "think about": "consider",
    "show": "demonstrate",
    "tell": "inform",
    "say": "state",
    "need to": "must",
    "like i said": "as previously stated",
    "to sum up": "in conclusion",
    "anyway": "nonetheless",
    "a bit": "slightly",
    "okay": "acceptable",
    "cool": "interesting",
    "awesome": "remarkable",
    "i think that": "It is believed that",
    "i believe": "It is considered that",
    "i feel": "It appears that",
    "i guess": "It is assumed that",
    "i'm gonna": "I am going to",
    "i'm gonna go": "I intend to leave",
    "i want to": "I would like to",
    "i don't know": "It is uncertain",
    "i don't think": "It is unlikely that",
    "i can't": "It is not possible to",
    "i'm sure": "It is evident that",
    "i'm not sure": "It is unclear whether",
    "i hope": "It is hoped that",
    "i guess so": "That appears to be the case",
    "you can see": "It can be observed",
    "as you can see": "As can be observed",
    "you should": "It is recommended that",
    "you have to": "It is necessary to",
    "you need to": "It is essential to",
    "you might": "It is possible that",
    "you could": "It may be possible to",
    "guy": "individual",
    "girl": "young woman",
    "kids these days": "today's youth",
    "a bunch of": "a number of",
    "a lot": "numerous",
    "lots of": "a considerable amount of",
    "tons of": "a large quantity of",
    "way more": "significantly more",
    "way less": "considerably less",
    "pretty good": "adequate",
    "not bad": "acceptable",
    "get better": "improve",
    "get worse": "deteriorate",
    "get rid of": "eliminate",
    "keep on": "continue",
    "end up": "ultimately",
    "deal with it": "address the issue",
    "figure out": "determine",
    "freak out": "become alarmed",
    "mess up": "make an error",
    "screw up": "fail",
    "fix it": "resolve the issue",
    "do it again": "repeat the process",
    "go ahead": "proceed",
    "i'm tired of": "I am weary of",
    "don't want to": "prefer not to",
    "i like it": "I find it enjoyable",
    "i don't like": "I find it unappealing",
    "it's not fair": "It seems unjust",
    "i'm bored": "I am uninterested",
    "i'm busy": "I am occupied",
    "i'm done": "I have finished",
    "i messed up": "I made a mistake",
    "i feel bad": "I am remorseful",
    "i didn't mean to": "It was unintentional",
    "it looks good": "It appears appealing",
    "looks like": "seems to be",
    "sounds good": "That seems acceptable",
    "i'm okay with that": "I find that acceptable",
    "i agree": "I concur",
    "i don't agree": "I disagree",
    "i'll try": "I will attempt",
    "i guess we can": "It seems possible",
    "can i": "May I",
    "should i": "Would it be appropriate for me to",
    "i'm thinking": "It is being considered that",
    "i was thinking": "It was being considered that",
    "i feel like": "It seems that",
    "i don't feel like": "I am disinclined to",
    "i don't wanna": "I prefer not to",
    "i don't wanna go": "I prefer not to attend",
    "i wanna try": "I would like to attempt",
    "we gotta": "We must",
    "we're gonna": "We are going to",
    "we should": "It is advisable that we",
    "we can": "It is possible for us to",
    "it's like": "It resembles",
    "it's kinda like": "It is somewhat similar to",
    "he's gonna": "He is going to",
    "she wants to": "She intends to",
    "you better": "It is recommended that you",
    "you gotta": "You are required to",
    "can't do this": "This is not feasible",
    "don't know": "It is not known",
    "don't care": "This is considered irrelevant",
    "i'm not sure if": "It is uncertain whether",
    "let's see": "Let us examine",
    "that's fine": "That is acceptable",
    "sounds nice": "That seems agreeable",
    "i'm gonna do it": "I intend to complete it",
    "i'm gonna try": "I plan to attempt",
    "i'm not sure": "It is uncertain",
    "i'm fine": "I am well",
    "i'm not fine": "I am unwell",
    "i'm done with it": "I have completed it",
    "you gotta try": "It is recommended that you attempt",
    "you should go": "It is advisable that you attend",
    "let's go": "Let us proceed",
    "let me know": "Please inform me",
    "let's take a look": "Let us examine",
    "that's not right": "That is inaccurate",
    "this sucks": "This is unsatisfactory",
    "what's up": "How are you",
    "i got it": "I understand",
    "it doesn't make sense": "It appears illogical",
    "it makes sense": "It is reasonable",
    "i'm broke": "I am financially struggling",
    "i'm busy": "I am currently occupied",
    "i'm tired": "I am fatigued",
    "i'm confused": "I am uncertain",
    "i'm bored": "I am uninterested",
    "i'm happy": "I am content",
    "i'm sad": "I am feeling down",
    "it's fine": "It is acceptable",
    "that's cool": "That is interesting",
    "not sure": "Uncertain",
    "sure thing": "Certainly",
    "i'm": "i am",
    "it's": "it is"
}

# Fungsi sinonim
# def get_synonyms(word):
#     synonyms = set()
#     for syn in wordnet.synsets(word):
#         for lemma in syn.lemmas():
#             if lemma.name().lower() != word.lower():
#                 synonyms.add(lemma.name().replace('_', ' '))
#     return list(synonyms)

# Fungsi grammar
def check_grammar(text):
    matches = tool.check(text)
    suggestions = []
    for match in matches:
        suggestions.append({
            "error": text[match.offset : match.offset + match.errorLength],
            "message": match.message,
            "suggestion": match.replacements
        })
    return suggestions

# Fungsi vocabulary checker
def check_common_words(text):
    vocab_suggestions = []
    words = text.lower().split()
    for word in words:
        for key in common_words:
            if key in word:
                vocab_suggestions.append({
                    "word": key,
                    "suggestions": common_words[key]
                })
    return vocab_suggestions

# Fungsi style checker
def check_style(text):
    style_suggestions = []
    lowered = text.lower()
    for informal, formal in style_patterns.items():
        if informal in lowered:
            style_suggestions.append({
                "informal": informal,
                "suggestion": formal
            })
    return style_suggestions

# Fungsi skor grammar
def grammar_score(total_words, total_errors):
    if total_words == 0:
        return 0
    error_ratio = total_errors / total_words
    score = max(0, 100 - (error_ratio * 100))
    return round(score, 2)

def get_readability(text):
    return round(textstat.flesch_reading_ease(text), 2)

def suggest_text_improvement(text):
    # Perbaiki grammar menggunakan suggestion pertama dari LanguageTool
    matches = tool.check(text)
    corrected_text = text
    offset_correction = 0  # untuk sesuaikan posisi setelah diganti

    for match in matches:
        if match.replacements:
            start = match.offset + offset_correction
            end = start + match.errorLength
            suggestion = match.replacements[0]
            corrected_text = corrected_text[:start] + suggestion + corrected_text[end:]
            offset_correction += len(suggestion) - match.errorLength

    # Perbaiki vocabulary umum
    for key, suggestions in common_words.items():
        replacement = suggestions[0]
        corrected_text = corrected_text.replace(f" {key} ", f" {replacement} ")

    # Perbaiki style informal
    for informal, formal in style_patterns.items():
        corrected_text = corrected_text.replace(f" {informal} ", f" {formal} ")

    return corrected_text


# === STREAMLIT UI ===
st.set_page_config(page_title="AI Writing Assistant", layout="wide")
st.title("📘 AI Writing Assistant")
st.write("Masukkan esai/artikel kamu, dan sistem akan memberikan saran:")
st.write("Pilih aspek yang ingin kamu evaluasi dari tulisanmu:")

options = st.multiselect(
    "✅ Pilih satu atau lebih:",
    ["Grammar", "Sinonim", "Vocabulary", "Style", "Readability"],
    default=["Grammar", "Sinonim", "Vocabulary", "Style", "Readability"]
)

user_text = st.text_area("✍️ Tulis teks kamu di sini:", height=150)

if st.button("🔍 Cek Teks"):
    if user_text.strip() == "":
        st.warning("⚠️ Masukkan teks terlebih dahulu.")
    else:
        total_words = len(user_text.split())

        if "Grammar" in options:
            st.subheader("🛠️ Grammar Check")
            grammar_issues = check_grammar(user_text)
            total_errors = len(grammar_issues)
            st.markdown(f"📊 **Grammar Score**: `{grammar_score(total_words, total_errors)} / 100`")

            if not grammar_issues:
                st.success("✅ Tidak ditemukan kesalahan grammar.")
            else:
                for issue in grammar_issues:
                    st.markdown(f"- ❌ **{issue['error']}** → 💡 {issue['message']}")
                    if issue['suggestion']:
                        st.markdown(f"  🔁 Saran: `{issue['suggestion'][0]}`")

        # if "Sinonim" in options:
        #     st.subheader("🔤 Vocabulary Enhancement (Sinonim Kata)")
        #     for word in user_text.split():
        #         syns = get_synonyms(word)
        #         if syns:
        #             st.markdown(f"- **{word}** → 🔁 Contoh sinonim: {', '.join(syns[:3])}")

        if "Vocabulary" in options:
            st.subheader("🧠 Vocabulary Improvement")
            vocab_check = check_common_words(user_text)
            if not vocab_check:
                st.info("Tidak ada kata terlalu umum yang perlu diganti.")
            else:
                for item in vocab_check:
                    st.markdown(f"- **{item['word']}** → 💡 Ganti dengan: `{', '.join(item['suggestions'])}`")

        if "Style" in options:
            st.subheader("🎨 Style Suggestion")
            style_check = check_style(user_text)
            if not style_check:
                st.info("Tidak ada gaya informal terdeteksi.")
            else:
                for item in style_check:
                    st.markdown(f'- ✏️ Gunakan gaya lebih formal untuk **"{item["informal"]}"** → 💡 `{item["suggestion"]}`')

        if "Readability" in options:
            st.subheader("📚 Readability Score")
            readability = get_readability(user_text)
            st.markdown(f"📏 Tingkat keterbacaan teks kamu: **{readability}**")
            if readability >= 60:
                st.success("✅ Teks cukup mudah dibaca.")
            else:
                st.warning("⚠️ Teks cukup sulit dibaca, pertimbangkan untuk menyederhanakan kalimat.")
                
            st.subheader("📝 Teks yang Telah Ditingkatkan")
            improved_text = suggest_text_improvement(user_text)
            st.text_area("📄 Hasil Perbaikan Otomatis:", value=improved_text, height=200)
