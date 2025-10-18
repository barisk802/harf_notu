import streamlit as st

st.title("📘 Harf Notu Hesaplama Sistemi")

st.write("Vize 1 ve Final notunuzu giriniz:")

# Kullanıcıdan girişleri al
vize1 = st.number_input("Vize 1:", min_value=0, max_value=100, step=1)
final = st.number_input("Final:", min_value=0, max_value=100, step=1)

# Hesapla butonu
if st.button("Hesapla"):
    genel_not = vize1 * 3/10 + final * 7/10
    st.write(f"Genel Notunuz: **{genel_not:.2f}**")

    # Harf notu koşulları
    if genel_not >= 90:
        st.success("Harf Notunuz: **AA 🎯**")
    elif genel_not >= 85:
        st.info("Harf Notunuz: **BA**")
    elif genel_not >= 80:
        st.info("Harf Notunuz: **BB**")
    elif genel_not >= 75:
        st.warning("Harf Notunuz: **CB**")
    elif genel_not >= 70:
        st.warning("Harf Notunuz: **CC**")
    elif genel_not >= 65:
        st.warning("Harf Notunuz: **DC**")
    elif genel_not >= 60:
        st.warning("Harf Notunuz: **DD**")
    elif genel_not >= 30:
        st.warning("Harf Notunuz: **FD**")
    else:
        st.error("Harf Notunuz: **FF ❌**")


