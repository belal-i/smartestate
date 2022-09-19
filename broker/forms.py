from django.utils import translation
from django import forms
# TODO: In future, it might be cleaner to use this, if possible.
# from modeltranslation.forms import TranslationModelForm



class ListingSearchForm(forms.Form):


    # These form fields go hand in hand with the parameters supported by
    # broker.utils.filter_search_listing

    listing_type = forms.ChoiceField(
        # TODO: Figure out how to translate these
        choices=[
            ('', '--'),
            ('rental', 'Rental'),
            ('for_sale', 'For sale'),
        ],
        label={
            'en': 'Listing type',
            'de': 'Angebotstyp',
            'fr': 'Type d\'offre',
            'es': 'Tipo de oferta',
            'it': 'Tipo di offerta',
        },
        widget=forms.Select(attrs={'class': 'form-toggle-field'}),
        required=False
    )
    max_rental_price = forms.IntegerField(
        label={
            'en': 'Maximum rent',
            'de': 'Maximale Miete',
            'fr': 'Loyer maximal',
            'es': 'Alquiler máximo',
            'it': 'Affitto massimo',
        },
        required=False)
    min_rental_price = forms.IntegerField(
        label={
            'en': 'Minimum rent',
            'de': 'Minimale Miete',
            'fr': 'Loyer minimal',
            'es': 'Alquiler mínimo',
            'it': 'Affitto minimo',
        },
        required=False)
    max_security_deposit = forms.IntegerField(
        label={
            'en': 'Maximum security deposit',
            'de': 'Maximale Kaution',
            'fr': 'Dépôt maximal',
            'es': 'Depósito máximo',
            'it': 'Deposito massimo',
        },
        required=False)
    min_security_deposit = forms.IntegerField(
        label={
            'en': 'Minimum security deposit',
            'de': 'Minimale Kaution',
            'fr': 'Dépôt minimal',
            'es': 'Depósito mínimo',
            'it': 'Deposito minimo',
        },
        required=False)
    max_for_sale_price = forms.IntegerField(
        label={
            'en': 'Maximum for sale price',
            'de': 'Maximaler Kaufpreis',
            'fr': 'Prix d\'achat maximal',
            'es': 'Precio máximo de compra',
            'it': 'Prezzo massimo di acquisto',
        },
        required=False)
    min_for_sale_price = forms.IntegerField(
        label={
            'en': 'Minimum for sale price',
            'de': 'Minimaler Kaufpreis',
            'fr': 'Prix d\'achat minimal',
            'es': 'Precio mínimo de compra',
            'it': 'Prezzo minimo di acquisto',
        },
        required=False)
    max_minimum_down_payment = forms.IntegerField(
        label={
            'en': 'Highest acceptable minimum down payment',
            'de': 'Maximale zulässige Anzahlung',
            'fr': 'Dépôt de garantie maximum acceptable',
            'es': 'Depósito de seguridad máximo aceptable',
            'it': 'Deposito cauzionale massimo accettabile',
        },
        required=False
    )
    min_minimum_down_payment = forms.IntegerField(
        label={
            'en': 'Lowest acceptable minimum down payment',
            'de': 'Minimale zulässige Anzahlung',
            'fr': 'Dépôt de garantie minimum acceptable',
            'es': 'Depósito de seguridad mínimo aceptable',
            'it': 'Deposito cauzionale minimo accettabile',
        },
        required=False
    )
    earliest_date_available = forms.DateField(
        label={
            'en': 'Earliest date available',
            'de': 'Frühestes Verfügbarkeitsdatum',
            'fr': 'Première date de disponibilité',
            'es': 'Fecha de disponibilidad más temprana',
            'it': 'Prima data di disponibilità',
        },
        required=False
    )
    latest_date_available = forms.DateField(
        label={
            'en': 'Latest date available',
            'de': 'Spätestes Verfügbarkeitsdatum',
            'fr': 'Dernière date de disponibilité',
            'es': 'Última fecha de disponibilidad',
            'it': 'Ultima data di disponibilità',
        },
        required=False
    )
    minimum_months = forms.IntegerField(
        label={
            'en': 'Minimum number of months',
            'de': 'Mindestmietzeit in Monaten',
            'fr': 'Durée de location minimale en mois',
            'es': 'Periodo mínimo de alquiler en meses',
            'it': 'Periodo minimo di noleggio in mesi',
        },
        required=False
    )
    maximum_months = forms.IntegerField(
        label={
            'en': 'Maximum number of months',
            'de': 'Höchstmietzeit in Monaten',
            'fr': 'Durée de location maximale en mois',
            'es': 'Periodo máximo de alquiler en meses',
            'it': 'Periodo massimo di noleggio in mesi',
        },
        required=False
    )
    min_number_of_people = forms.IntegerField(
        label={
            'en': 'Minimum number of people',
            'de': 'Mindestanzahl Personen',
            'fr': 'Nombre minimum de personnes',
            'es': 'Número mínimo de personas',
            'it': 'Numero minimo di persone',
        },
        required=False
    )
    max_number_of_people = forms.IntegerField(
        label={
            'en': 'Maximum number of people',
            'de': 'Höchstanzahl Personen',
            'fr': 'Nombre maximum de personnes',
            'es': 'Número máximo de personas',
            'it': 'Numero massimo di persone',
        },
        required=False
    )
    pets_ok = forms.BooleanField(
        label={
            'en': 'Pets OK',
            'de': 'Haustiere OK',
            'fr': 'Animaux domestiques OK',
            'es': 'Mascotas OK',
            'it': 'Animali domestici OK',
        },
        required=False,
    )
    is_primary = forms.BooleanField(
        label={
            'en': 'Apartment is the only / primary one in the house',
            'de': 'Wohnung ist die einzige im Haus',
            'fr': 'L\'appartement est le seul de la maison',
            'es': 'El apartamento es el único en la casa',
            'it': 'L\'appartamento è l\'unico in casa',
        },
        required=False,
    )
    min_number_of_rooms = forms.IntegerField(
        label={
            'en': 'Minimum number of rooms',
            'de': 'Mindestanzahl Räume',
            'fr': 'Nombre minimum de chambres',
            'es': 'Número mínimo de habitaciones',
            'it': 'Numero minimo di camere',
        },
        required=False
    )
    max_number_of_rooms = forms.IntegerField(
        label={
            'en': 'Maximum number of rooms',
            'de': 'Höchstanzahl Räume',
            'fr': 'Nombre maximum de chambres',
            'es': 'Número máximo de habitaciones',
            'it': 'Numero massimo di camere',
        },
        required=False
    )
    min_size_sq_m = forms.IntegerField(
        label={
            'en': 'Minimum size (sq. m)',
            'de': 'Minimale Größe (QM.)',
            'fr': 'Taille minimale (m²)',
            'es': 'Tamaño mínimo (m2)',
            'it': 'Dimensioni minime (mq)',
        },
        required=False
    )
    max_size_sq_m = forms.IntegerField(
        label={
            'en': 'Maximum size (sq. m)',
            'de': 'Maximale Größe (QM.)',
            'fr': 'Taille maximale (m²)',
            'es': 'Tamaño máximo (m2)',
            'it': 'Dimensioni massime (mq)',
        },
        required=False
    )
    has_internet = forms.BooleanField(
        label={
            'en': 'Internet is included',
            'de': 'Internet vorhanden',
            'fr': 'Internet disponible',
            'es': 'Internet disponible',
            'it': 'Internet disponibile',
        },
        required=False,
    )
    is_furnished = forms.BooleanField(
        label={
            'en': 'Apartment must be furnished',
            'de': 'Wohnung muss möbliert sein',
            'fr': 'L\'appartement doit être meublé',
            'es': 'El apartamento debe estar amueblado',
            'it': 'L\'appartamento deve essere arredato',
        },
        required=False,
    )
    min_date_of_construction = forms.DateField(
        label={
            'en': 'Earliest acceptable date of construction',
            'de': 'Frühestes zulässiges Baujahr',
            'fr': 'Date de construction la plus proche acceptable',
            'es': 'Primera fecha de construcción aceptable',
            'it': 'Prima data accettabile di costruzione',
        },
        required=False
    )
    max_date_of_construction = forms.DateField(
        label={
            'en': 'Latest acceptable date of construction',
            'de': 'Spätestes zulässiges Baujahr',
            'fr': 'Dernière date acceptable de construction',
            'es': 'Última fecha de construcción aceptable',
            'it': 'Ultima data accettabile di costruzione',
        },
        required=False
    )

class SeekingSearchForm(forms.Form):

    # These form fields go hand in hand with the parameters supported by
    # broker.utils.filter_search_seeking

    seeking_type = forms.ChoiceField(
        # TODO: Figure out how to translate these
        choices=[
            ('', '--'),
            ('rental', 'Rental'),
            ('for_sale', 'For sale'),
        ],
        label={
            "en": "Seeking type",
            "de": "Gesuchstyp",
            "fr": "Type de demande",
            "es": "Tipo de aplicacion",
            "it": "Tipo di applicazione",
        },
        widget=forms.Select(attrs={'class': 'form-toggle-field'}),
        required=False
    )
    max_rent = forms.IntegerField(
        label={
            "en": "Maximum rent",
            "de": "Maximale Miete",
            "fr": "Loyer maximal",
            "es": "Alquiler máximo",
            "it": "Affitto massimo",
        },
        required=False)
    min_rent = forms.IntegerField(
        label={
            "en": "Minimum rent",
            "de": "Minimale Miete",
            "fr": "Loyer minimal",
            "es": "Alquiler mínimo",
            "it": "Affitto minimo",
        },
        required=False)
    max_purchase_price = forms.IntegerField(
        label={
            "en": "Maximum purchase price",
            "de": "Maximaler Kaufpreis",
            "fr": "Prix d\'achat maximal",
            "es": "Precio máximo de compra",
            "it": "Prezzo massimo di acquisto",
        },
        required=False
    )
    min_purchase_price = forms.IntegerField(
        label={
            "en": "Minimum purchase price",
            "de": "Minimaler Kaufpreis",
            "fr": "Prix d\'achat minimal",
            "es": "Precio mínimo de compra",
            "it": "Prezzo minimo di acquisto",
        },
        required=False
    )
    min_number_of_rooms = forms.IntegerField(
        label={
            "en": "Minimum number of rooms",
            "de": "Minimale Anzahl Räume",
            "fr": "Nombre minimum de chambres",
            "es": "Número mínimo de habitaciones",
            "it": "Numero minimo di camere",
        },
        required=False
    )
    max_number_of_rooms = forms.IntegerField(
        label={
            "en": "Maximum number of rooms",
            "de": "Maximale Anzahl Räume",
            "fr": "Nombre maximum de chambres",
            "es": "Número máximo de habitaciones",
            "it": "Numero massimo di camere",
        },
        required=False
    )
    min_size_sq_m = forms.IntegerField(
        label={
            "en": "Minimum size (sq. m)",
            "de": "Minimale Größe (QM.)",
            "fr": "Taille minimale (m²)",
            "es": "Tamaño mínimo (m2)",
            "it": "Dimensioni minime (mq)",
        },
        required=False
    )
    max_size_sq_m = forms.IntegerField(
        label={
            "en": "Maximum size (sq. m)",
            "de": "Maximale Größe (QM.)",
            "fr": "Taille maximale (m²)",
            "es": "Tamaño máximo (m2)",
            "it": "Dimensioni massime (mq)",
        },
        required=False
    )
    min_number_of_persons = forms.IntegerField(
        label={
            "en": "Minimum number of persons",
            "de": "Minimale Anzahl Personen",
            "fr": "Nombre minimum de personnes",
            "es": "Número mínimo de personas",
            "it": "Numero minimo di persone",
        },
        required=False
    )
    max_number_of_persons = forms.IntegerField(
        label={
            "en": "Maximum number of persons",
            "de": "Maximale Anzahl Personen",
            "fr": "Nombre maximum de personnes",
            "es": "Número máximo de personas",
            "it": "Numero massimo di persone",
        },
        required=False
    )
    min_starting_date = forms.DateField(
        label={
            "en": "Earliest starting date",
            "de": "Frühestes Startdatum",
            "fr": "Date de début au plus tôt",
            "es": "Fecha de inicio más temprana",
            "it": "Prima data di inizio",
        },
        required=False
    )
    max_starting_date = forms.DateField(
        label={
            "en": "Latest starting date",
            "de": "Spätestes Startdatum",
            "fr": "Dernière date de début",
            "es": "Última fecha de inicio",
            "it": "Ultima data di inizio",
        },
        required=False
    )
    min_ending_date = forms.DateField(
        label={
            "en": "Earliest ending date",
            "de": "Frühestes Enddatum",
            "fr": "Date de fin au plus tôt",
            "es": "Fecha de finalización más temprana",
            "it": "Prima data di fine",
        },
        required=False
    )
    max_ending_date = forms.DateField(
        label={
            "en": "Latest ending date",
            "de": "Spätestes Enddatum",
            "fr": "Dernière date de fin",
            "es": "Última fecha de finalización",
            "it": "Ultima data di fine",
        },
        required=False
    )
    min_number_of_months = forms.IntegerField(
        label={
            "en": "Minimum number of months",
            "de": "Mindestmietzeit in Monaten",
            "fr": "Durée de location minimale en mois",
            "es": "Periodo mínimo de alquiler en meses",
            "it": "Periodo minimo di noleggio in mesi",
        },
        required=False
    )
    max_number_of_months = forms.IntegerField(
        label={
            "en": "Maximum number of months",
            "de": "Maximale Mietzeit in Monaten",
            "fr": "Durée de location maximale en mois",
            "es": "Periodo máximo de alquiler en meses",
            "it": "Periodo massimo di noleggio in mesi",
        },
        required=False
    )
    must_be_furnished = forms.BooleanField(
        label={
            "en": "Apartment must be furnished",
            "de": "Wohnung muss möbliert sein",
            "fr": "L'appartement doit être meublé",
            "es": "El apartamento debe estar amueblado",
            "it": "L'appartamento deve essere arredato",
        },
        required=False
    )
    must_have_internet = forms.BooleanField(
        label={
            "en": "Apartment must have internet",
            "de": "Wohnung muss Internet haben",
            "fr": "L'appartement doit avoir Internet",
            "es": "El apartamento debe tener internet.",
            "it": "L'appartamento deve avere internet",
        },
        required=False
    )
    is_smoker = forms.BooleanField(
        label={
            "en": "Tenant is smoker",
            "de": "Mieter ist Raucher",
            "fr": "Le locataire est fumeur",
            "es": "El inquilino es fumador",
            "it": "L'inquilino è un fumatore",
        },
        required=False
    )
    has_pets = forms.BooleanField(
        label={
            "en": "Tenant has pets",
            "de": "Mieter hat Haustiere",
            "fr": "Le locataire a des animaux de compagnie",
            "es": "El inquilino tiene mascotas",
            "it": "L'inquilino ha animali domestici",
        },
        required=False
    )
    min_age = forms.IntegerField(
        label={
            "en": "Minimum age of tenant",
            "de": "Mindestalter von Mieter",
            "fr": "Âge minimum du locataire",
            "es": "Edad mínima del inquilino",
            "it": "Età minima dell'inquilino",
        },
        required=False
    )
    max_age = forms.IntegerField(
        label={
            "en": "Maximum age of tenant",
            "de": "Maximales Alter von Mieter",
            "fr": "Âge maximum du locataire",
            "es": "Edad máxima del inquilino",
            "it": "Età massima dell'inquilino",
        },
        required=False
    )
