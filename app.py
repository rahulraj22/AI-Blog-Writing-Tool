import openai
import streamlit as st
# api key for openai here: https://platform.openai.com/account/api-keys
API_KEY = st.sidebar.text_input('Enter your API key')
openai.api_key = API_KEY

# openai.api_key = ''

def main():
    st.sidebar.header('AI Blog Writing Tool')
    st.sidebar.info('An AI tool that can generate blog content')
    st.sidebar.info('Start with the first option\n before you proceed to the next.')
    op = st.sidebar.selectbox('Steps', ['topics', 'section', 'content'])
    if op == 'topics':
        topics()
    elif op == 'section':
        section()
    else:
        content()

def topics():
    st.header('AI Blog Writing Tool')
    st.info('To generate blog topic, please follow the pattern given below:')
    prompt = st.text_area('Write your words', height=50, value='Generate blog topic on data science with Python')
    if st.button('Send'):
        st.text(BlogTopics(prompt))

def section():
    st.header('AI Blog Writing Tool')
    st.info('To generate blog section, please follow the pattern given below:')
    prompt = st.text_area('Write your words', height=50, value='Write blog sections\n\nBlog topic: ')
    if st.button('Send'):
        st.text(BlogSections(prompt))


def content():
    st.header('AI Blog Writing Tool')
    st.info('To generate blog content, please follow the pattern given below:')
    prompt = st.text_area('Write your words', height=50, value="Expand the blog section in a professional tone \n\nBlog Topic:\n\nSection:")
    if st.button('Send'):
        st.text(BlogContent(prompt))

def BlogTopics(prompt):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt=prompt,
      temperature=0.7,
      max_tokens=100,  # max-tokens implies no. of characters we want chatGPT(model) to generate
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response.choices[0].text

def BlogSections(prompt):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt=prompt,
      temperature=0.6,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response.choices[0].text


def BlogContent(prompt):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt=prompt,
      temperature=0.7,
      max_tokens=400,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response.choices[0].text



if __name__ == '__main__':
    main()
