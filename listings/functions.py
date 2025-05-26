def validate_search_params(input_dict):
    return_dict = input_dict.copy().dict()
    str_fields = [
        'listing_type',
        'earliest_date_available',
        'latest_date_available',
        'max_date_of_construction',
        'min_date_of_construction',
    ]
    bool_fields = [
        'pets_ok',
        'is_primary',
        'has_internet',
        'is_furnished',
    ]
    int_fields = [
        'minimum_months',
        'maximum_months',
        'max_number_of_people',
        'min_number_of_people',
        'max_number_of_rooms',
        'min_number_of_rooms',
        'max_size_sq_m',
        'min_size_sq_m',
    ]
    float_fields = [
        'max_rental_price',
        'min_rental_price',
        'max_security_deposit',
        'min_security_deposit',
        'max_for_sale_price',
        'min_for_sale_price',
        'min_minimum_down_payment',
        'max_minimum_down_payment',
    ]

    for field in str_fields:
        try:
            if return_dict[field] == '':
                return_dict.pop(field)
        except KeyError:
            pass

    for field in bool_fields:
        try:
            if return_dict[field] == "on":
                return_dict[field] = True
            else:
                return_dict.pop(field)

        except KeyError:
            pass
        except ValueError:
            return_dict.pop(field)

    for field in int_fields:
        try:
            return_dict[field] = int(return_dict[field])
        except KeyError:
            pass
        except ValueError:
            return_dict.pop(field)

    for field in float_fields:
        try:
            return_dict[field] = float(return_dict[field])
        except KeyError:
            pass
        except ValueError:
            return_dict.pop(field)

    return return_dict
