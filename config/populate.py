from .models import Config

def populate():
    did_init = Config.objects.get_or_create(
        config_var='did_init')[0]
    if did_init.config_val == 'no':
        site_title = "SmartEstate"
        cover_text = """Welcome to SmartEstate!\n

        SmartEstate lets real estate owners, brokers, managers, landlords, etc. manage their listings all from one conventient, cloud native web app.

Please stay tuned, more info is coming soon.
        """
        about_text = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
        """
        c_site_title = Config(config_var='site_title', config_val=site_title)
        c_cover_text = Config(config_var='cover_text', config_val=cover_text)
        c_about_text = Config(config_var='about_text', config_val=about_text)

        c_site_title.save()
        c_cover_text.save()
        c_about_text.save()

        did_init.config_val = 'yes'
        did_init.save()
