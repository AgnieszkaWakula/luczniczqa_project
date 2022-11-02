class StartPageLocators:

    START_PAGE_HEADER = "//h1[@class='h3 text-muted']"
    START_PAGE_APP_STATUS_INDICATOR = "//h1[text()[contains(.,'The status')]]/following-sibling::h1"
    START_PAGE_SET_ONLINE_BUTTON = "//button[@id='btn_online']"
    START_PAGE_SET_OFFLINE_BUTTON = "//button[@id='btn_offline']"
    START_PAGE_STUDENT_TABLE_LAST_ROW = "//table[@id='students']/descendant::tr[last()]"
    START_PAGE_UNIVERSITY_TABLE_LAST_ROW = "//table[@id='universities']/descendant::tr[last()]"