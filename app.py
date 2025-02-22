import streamlit as st
import pandas as pd


st.set_page_config(layout='wide', page_title='HeartAttackRisk', page_icon='🏘')


st.title(':rainbow[Heart]:red[AttackRisk]')


home_tab, predict_tab = st.tabs(["Ana Sayfa", "Risk Tahmin"])

# home tab
home_tab.title('❤️Heart Attack')
col1, col2 = home_tab.columns([1, 1])
col1.image(
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnFvYzRoc3RwN2wyYm4waTFib2o2YTlvdmEwcXpoc2x5amdibmJzdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oDXJPqRpJTf7qsxc3l/giphy.gif")
col1.subheader("Aradığınız Ev İşte Burada")
col1.markdown(
    'MiuulBnG şirketi olarak sizlere istediğiniz özelliklere sahip evleri sunuyoruz. Ayrıca evini bizimle kiraya vermek isteyenlere ev sahiplerimiz için en uygun kira tutarını belirliyoruz. '
    'Hem size kazandırıyoruz hem de sizinle kazanıyoruz')

col2.subheader("Gidecek Yerin mi Yok İşte Tam Aradığın Yer")
col2.markdown(
    "Gidecek yer bulmak bazen zorlayıcı olabilir, ancak endişelenmeyin; aradığınız yer burada! İster şehrin kalbinde hareketli bir yaşam alanı arıyor olun, ister huzur dolu bir kaçış noktası peşinde olun, size en uygun konaklama seçeneklerini sunmak için buradayız. Bu sayfada, ihtiyacınıza ve beklentilerinize göre özenle seçilmiş evler bulacaksınız. Her bir seçenek, konforunuzu ve memnuniyetinizi ön planda tutarak, kendinizi evinizde gibi hissetmeniz için tasarlandı. "
    "Size sadece uygun olanı seçmek kaldı; gerisini biz hallederiz. Keyifli ve unutulmaz bir konaklama deneyimi için doğru yerdesiniz!.")
col2.image("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnl6dGdkNHNqNXF2ajJ5bGZta2VnajNhYzUycDRvdHg3ZmJhMjNtcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/d2d3Tx0Ltc3HIZJgua/giphy.gif")
col1.image(
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDd4OHJ0Zm5ubW9kcGVqODNzYjZoaG1zMHIyMGp1ZXV6emJoN2p0NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WoFPRKUTbXMClPCSjl/giphy.gif")
col1.subheader("En İyi Ev Sahiplerine mi Sahibiz")
col1.markdown(
    "Aylık olarak güncellediğimiz Süper 10 ev sahibi listesini gördünüz mü? Görüntülemek için superhostlar sayfasını ziyaret etmeyi unutmayın.")


col1.subheader("Mük20 Listemiz")

