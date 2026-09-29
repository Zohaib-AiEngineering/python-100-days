import io
import streamlit as st
import requests 
from bs4 import BeautifulSoup
import pandas as pd

st.title("Web Scraper")
url = st.text_input("Enter website URL")
st.write("URL:", url)


if st.button("Scrape Products"):
    # Input Validation
    if not url:
        st.warning("⚠️ Baraye karam pehle koi URL enter karein.")
    elif not url.startswith(("http://", "https://")):
        st.warning("⚠️ URL ke shuru mein 'http://' ya 'https://' hona zaroori hai.")
    else:
        # Try block shuru
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        

           
            
            soup = BeautifulSoup(response.text, "html.parser")
            products = soup.find_all("div", class_="product")
            
            if not products:
                st.error("❌ Is website par '<div class=\"product\">' wala data nahi mila.")
            else:
                st.success("✅ Website fetched successfully!")

                scraped_data = []
                for item in products:
                    name = item.find("h2").text if item.find("h2") else "N/A"
                    price = item.find("p").text if item.find("p") else "N/A"
                    
                    scraped_data.append({
                        "Product Name": name,
                        "Price": price
                    })
                
                df = pd.DataFrame(scraped_data)
                
                st.write("### Extracted Data Preview:")
                st.dataframe(df, use_container_width=True)
                
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                    df.to_excel(writer, index=False, sheet_name='Products Data')

                st.info("Excel file successfully memory (RAM) mein ban gia ha")
                st.download_button(
                    label="Download Excel File",
                    data=buffer.getvalue(),
                    file_name="scraped_products.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )
                
        # Except blocks bilkul 'try' ki seedh mein hain
        except requests.exceptions.RequestException as e:
            st.error(f"Network Error: Website sy connect ni ho rha")
        except Exception as e:
            st.error(f"Ek unexpected error aa ya :{e}")