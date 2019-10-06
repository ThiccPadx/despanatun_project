// Public config

var antiCapthaPredefinedApiKey = '';

var defaultConfig = {
    // settings
    enable: true,
    account_key: antiCapthaPredefinedApiKey,
    auto_submit_form: false,
    solve_recaptcha2: true,
    solve_invisible_recaptcha: true,
    dont_reuse_recaptcha_solution: true,
    solve_funcaptcha: false, // off by default
    start_recaptcha2_solving_when_challenge_shown: false,
    solve_only_presented_recaptcha2: false,
    solve_geetest: true,
    use_predefined_image_captcha_marks: true,
    play_sounds: false,

    use_recaptcha_accelerator: true,

    use_recaptcha_precaching: false,
    k_precached_solution_count_min: 2,
    k_precached_solution_count_max: 4,

    /*
    user_proxy_protocol: '',
    user_proxy_server: '',
    user_proxy_port: '',
    user_proxy_login: '',
    user_proxy_password: '',
    */

    // status
    account_key_checked: antiCapthaPredefinedApiKey ? true : false, // set after account_key check
    free_attempts_left_count: 15 // move to config
};