import os

from fastapi import APIRouter
from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe import session, emailpassword, thirdparty
from supertokens_python.recipe.thirdparty import (
    ProviderInput,
    ProviderConfig,
    ProviderClientConfig,
    SignInAndUpFeature,
)

router = APIRouter(prefix="/auth")

init(
    app_info=InputAppInfo(
        app_name="MyApp",
        website_domain="http://localhost:2000",
        api_domain="http://localhost:8000",
        api_base_path="/auth",
        website_base_path="/auth",
    ),
    supertokens_config=SupertokensConfig(
        connection_uri="http://localhost:3567",
        api_key=os.environ["ST_API_KEY"],
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
                                    client_id=os.environ["GOOGLE_CLIENT_ID"],
                                    client_secret=os.environ["GOOGLE_CLIENT_SECRET"],
                                )
                            ],
                        )
                    )
                ]
            )
        ),
    ],
)
