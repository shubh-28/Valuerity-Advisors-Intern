# import os
# import google.generativeai as genai

# from dotenv import load_dotenv
# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # Create the model
# generation_config = {
#   "temperature": 1,
#   "top_p": 0.95,
#   "top_k": 64,
#   "max_output_tokens": 8192,
#   "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#   model_name="gemini-1.5-flash",
#   generation_config=generation_config,
# )

# history = []

# while True:


#     output = """Index Anchor Text                                                                                          Link
#     ========================================================================================================================
#     2     Investor Relations                                                                                   https://investor.snap.com/
#     [3468:4972:1023/171534.064:ERROR:ssl_client_socket_impl.cc(878)] handshake failed; returned -1, SSL error code 1, net_error -101
#     [3468:4972:1023/171534.079:ERROR:ssl_client_socket_impl.cc(878)] handshake failed; returned -1, SSL error code 1, net_error -101
#     81    Snap Inc. Announces Date of Third Quarter 2024 Results Conference Call                               https://investor.snap.com/news/news-details/2024/Snap-Inc.-Announces-Date-of-Third-Quarter-2024-Results-Conference-Call/default.aspx
#     82    Jim Lanzone Joins Snap Inc. Board of Directors                                                       https://investor.snap.com/news/news-details/2024/Jim-Lanzone-Joins-Snap-Inc.-Board-of-Directors/default.aspx
#     83    Snap Inc. Announces Second Quarter 2024 Financial Results                                            https://investor.snap.com/news/news-details/2024/Snap-Inc.-Announces-Second-Quarter-2024-Financial-Results/default.aspx
#     84    Snap Inc. Announces Date of Second Quarter 2024 Results Conference Call                              https://investor.snap.com/news/news-details/2024/Snap-Inc.-Announces-Date-of-Second-Quarter-2024-Results-Conference-Call/default.aspx
#     85    Snap Announces Pricing of $650 Million Convertible Senior Notes Offering Due 2030                    https://investor.snap.com/news/news-details/2024/Snap-Announces-Pricing-of-650-Million-Convertible-Senior-Notes-Offering-Due-2030/default.aspx     
#     93    Snap Inc.                                                                                            https://www.snap.com/
#     94    Careers                                                                                              https://careers.snap.com/
#     95    News                                                                                                 https://www.snap.com/news/
#     96    Support                                                                                              https://help.snapchat.com/
#     97    Community Guidelines                                                                                 https://values.snap.com/privacy/transparency/community-guidelines
#     98    Safety Center                                                                                        https://values.snap.com/safety/safety-center
#     99    Buy Ads                                                                                              https://ads.snapchat.com/getstarted
#     100   Advertising Policies                                                                                 https://www.snap.com/ad-policies/
#     101   Brand Guidelines                                                                                     https://www.snap.com/brand-guidelines
#     102   Promotions Rules                                                                                     https://help.snapchat.com/hc/articles/7047502545044
#     103   Privacy Center                                                                                       https://values.snap.com/privacy/privacy-center
#     104   Cookie Policy                                                                                        https://www.snap.com/cookie-policy/
#     105   Report Infringement                                                                                  https://help.snapchat.com/hc/articles/7012332110996
#     106   Lens Studio Terms                                                                                    https://lensstudio.snapchat.com/
#     107   Privacy Policy                                                                                       https://snap.com/en-US/privacy/privacy-policy/
#     108   Terms of Service                                                                                     https://snap.com/en-US/terms/
#     [3468:4972:1023/171535.666:ERROR:ssl_client_socket_impl.cc(878)] handshake failed; returned -1, SSL error code 1, net_error -101
#     109   Powered By Q4 Inc. 5.137.2.3
#     (opens in new window)                                                   https://www.q4inc.com/Powered-by-Q4/"""

#     prompt = """This code output currently contains news headlines with links but also includes extra text that isn't part of the headline. Please filter this data and provide only the headlines along with their links, removing any non-headline text. Structure the results in a numbered list format, with each item containing just the headline followed by its link. Only include items that resemble a news headline or a press release headline, omitting any irrelevant or extraneous information."""

#     chat_session = model.start_chat(
#     history=history
#     )

#     response = chat_session.send_message(output + " " + prompt)

#     model_response = response.text

#     print(model_response)
#     print()

#     history.append({"role": "user", "parts": [output + " " + prompt]})
#     history.append({"role": "model", "parts": [model_response]})
#     break


import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

history = []

while True:


    output = output_text

    prompt = """This code output currently contains news headlines with links but also includes extra text that isn't part of the headline. Please filter this data and provide only the headlines along with their links, removing any non-headline text. Structure the results in a numbered list format, with each item containing just the headline followed by its link. Only include items that resemble a news headline or a press release headline, omitting any irrelevant or extraneous information."""

    chat_session = model.start_chat(
    history=history
    )

    response = chat_session.send_message(output + " " + prompt)

    model_response = response.text

    print(model_response)
    print()

    history.append({"role": "user", "parts": [output + " " + prompt]})
    history.append({"role": "model", "parts": [model_response]})
    break