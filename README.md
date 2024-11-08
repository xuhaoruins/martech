# MarketingWriter

MarketingWriter is an intelligent marketing copy generation application built using Azure Container App, GitHub Models, and Streamlit.

## Features

- Generate complete marketing copy from user input ideas, bullet points, or product specifications.
- Support for selecting various product values and emotional values.
- Support for multiple language outputs, including English, Chinese, Japanese, and Korean.
- Generate copy based on user-specified age range and word count.
- Real-time display of generated copy.

## Implementation Details

### Tech Stack

- **Azure OpenAI**: Used to generate copy using Azure OpenAI service.
- **Streamlit**: Used to build the user interface.
- **dotenv**: Used to load environment variables.
- **Azure AI Inference**: Used to communicate with the Azure OpenAI service.

### Environment Variables

The application requires the following environment variables:

- `GITHUB_TOKEN`: GitHub token used to access the Azure OpenAI service.

### Deployment

1. Use azd init this template：

    ```sh
    azd init --template https://github.com/xuhaoruins/marketingwriter
    ```
2. update `.env` with your GitHub Token. You can create a new fine-grained PAT via the [Developer Settings section](https://github.com/settings/personal-access-tokens/new) in your account settings.
    
    ```sh
    GITHUB_TOKEN=your_github_token_xxxxxxxxxxxxxxxxxx
    ```

3. 部署应用：

    ```sh
    azd up
    ```