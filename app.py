import streamlit as st
import pandas as pd


st.set_page_config(layout='wide', page_title='HeartAttackRisk', page_icon='🏘')


st.title(':rainbow[Heart]:red[AttackRisk]')


home_tab, predict_tab = st.tabs(["Ana Sayfa", "Risk Tahmini"])

# home tab
home_tab.title('❤️‍🩹Heart Attack🩹🖤')
col1, col2 = home_tab.columns([1, 1])
col1.image("heart1.jpg")
col1.subheader("Kalp Krizi Nedir?")
col1.markdown(
    "Kalp krizi, kalbi besleyen koroner arterlerin tıkanması sonucu kalp kasına yeterli oksijenin ulaşamaması nedeniyle oluşan ciddi bir durumdur."
 "Genellikle damar sertliği (ateroskleroz) nedeniyle arterlerde plak birikmesiyle ortaya çıkar. Plaklar yırtıldığında pıhtı oluşarak damarı tamamen tıkayabilir." 
 "Göğüs ağrısı, nefes darlığı, terleme, mide bulantısı ve baş dönmesi gibi belirtilerle kendini gösterebilir. "
"Tedavi edilmezse kalp dokusunda geri dönüşü olmayan hasara yol açabilir ve ölümle sonuçlanabilir.")

col2.subheader("Kalp Krizini Ne Etkiler")
col2.markdown(
    "Kalp krizi riskini artıran birçok faktör vardır. Yaş ilerledikçe damarlar esnekliğini kaybeder ve tıkanma riski artar."
 "Erkeklerde risk daha yüksek olsa da menopoz sonrası kadınlarda da artış görülür. "
 "Sigara ve alkol kullanımı damarları daraltarak ve pıhtı oluşumunu artırarak krizi tetikleyebilir." 
 "Diyabet ve ani kan şekeri yükselmeleri damar duvarlarına zarar vererek süreci hızlandırır. Ailede kalp hastalığı öyküsü varsa genetik yatkınlık riski artırır." 
" Düzenli egzersiz yapmak ise kan dolaşımını iyileştirerek damar sağlığını korur ve kalp krizini önlemede önemli bir rol oynar.")
col2.image(
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjVuMmNtYjMzYzMzNGt0M2hsdW9xYnNiNmNwa2R1d203YTNxMmlwbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wzclsv1x3zhVS/giphy.gif")

