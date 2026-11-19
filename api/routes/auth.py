from fastapi import APIRouter
from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe import session, emailpassword, thirdparty
from supertokens_python.recipe.thirdparty import (
    ProviderInput,
    ProviderConfig,
    ProviderClientConfig,
    SignInAndUpFeature,
)

from api import config

# The SuperTokens middleware serves every /auth/* endpoint itself
# (/auth/signup, /auth/signin, /auth/signinup, /auth/signout, /auth/session/refresh, ...).
# This router only reserves the prefix.
router = APIRouter(prefix="/auth")

init(
    app_info=InputAppInfo(
        app_name="STAKED",
        website_domain=config.WEBSITE_DOMAIN,
        api_domain=config.API_DOMAIN,
        api_base_path="/auth",
        website_base_path="/auth",
    ),
    supertokens_config=SupertokensConfig(
        connection_uri=config.SUPERTOKENS_URI,
        api_key=config.SUPERTOKENS_API_KEY,
    ),
    framework="fastapi",
    mode="asgi",
    recipe_list=[
        session.init(),
        emailpassword.init(),
        thirdparty.init(
            sign_in_and_up_feature=SignInAndUpFeature(
                providers=[
                    ProviderInput(
                        config=ProviderConfig(
                            third_party_id="google",
                            clients=[
                                ProviderClientConfig(
                                    client_id=config.GOOGLE_CLIENT_ID,
                                    client_secret=config.GOOGLE_CLIENT_SECRET,
                                )
                            ],
                        )
                    )
                ]
            )
        ),
    ],
)
