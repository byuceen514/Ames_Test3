from tethys_sdk.base import TethysAppBase, url_map_maker


class MyThirdApp(TethysAppBase):
    """
    Tethys app class for my third app.
    """

    name = 'my third app'
    index = 'my_third_app:home'
    icon = 'my_third_app/images/icon.gif'
    package = 'my_third_app'
    root_url = 'my-third-app'
    color = '#e67e22'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='my-third-app',
                           controller='my_third_app.controllers.home'),
        )

        return url_maps