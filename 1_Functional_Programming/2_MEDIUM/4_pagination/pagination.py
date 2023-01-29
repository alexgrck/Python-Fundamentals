def paginate(input_, max_elements_on_page, page_number):
    if len(input_) > (page_number + 1) * max_elements_on_page:
        return input_[
            (page_number * max_elements_on_page) : (
                (page_number + 1) * max_elements_on_page
            )
        ]
    return input_[(page_number * max_elements_on_page) :]
