import io
import qrcode
import streamlit as st

st.set_page_config(page_title="8-Digit QR Generator", page_icon="📱")

st.title("📱 8-Digit Number QR Code Generator")
st.write("Koi bhi 8-digit number enter karein aur instant QR code hasil karein.")

# User Input
number_input = st.text_input(
    "8-Digit Number Dial Karein:", max_chars=8, placeholder="e.g. 12345678"
)

if number_input:
    if number_input.isdigit() and len(number_input) == 8:
        st.success(f"Valid Number Entered: **{number_input}**")

        # QR Code Generate
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=12,
            border=6,
        )
        qr.add_data(number_input)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Memory buffer mein save
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # Display Image (buf se bytes pass kar rahe hain)
        st.image(byte_im, caption=f"QR Code for {number_input}", width=250)

        # Download Button
        st.download_button(
            label="📥 QR Code Download Karein",
            data=byte_im,
            file_name=f"qr_{number_input}.png",
            mime="image/png",
        )
    else:
        st.error("⚠️ Baraye karam sirf **8 digits** (numbers) enter karein!")