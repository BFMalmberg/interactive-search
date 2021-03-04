import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        backend_error_flag: false,
        query_string: '',
        query_results: [],
        brands: [],
        median_price: 0,
        showResults: false,
    },
    actions: {
        async initQueryResults ({commit}, {random_seed}) {
            commit('UPDATE_QUESTIONS_LOADING', true);
            await Vue.http
                .get('questions/'+random_seed)
                .then(response => {
                    if (response.status === 200) {
                        commit('SET_QUESTIONS', response.data.questions);
                        commit('UPDATE_BACKEND_ERROR_FLAG', false);
                    }
                })
                .catch(error => {
                    console.error(error);
                    commit('UPDATE_BACKEND_ERROR_FLAG', true);
                });
            commit('UPDATE_QUESTIONS_LOADING', false);
        },
        async initMedianPrice ({commit}, {median_price}) {
            commit('SET_MEDIAN_PRICE', median_price());
        },
        setBackendErrorFlag ({commit}, {flag}) {
            commit('UPDATE_BACKEND_ERROR_FLAG', flag);
        },

    },
    mutations: {
        SET_MEDIAN_PRICE (state, median_price) {
            state.median_price = median_price;
        },
        SET_QUERY_RESULTS (state, query_results) {
            state.query_results = query_results;
        },
        UPDATE_BACKEND_ERROR_FLAG (state, flag) {
            state.backend_error_flag = flag;
        },
        UPDATE_QUESTIONS_LOADING (state, status) {
            state.questions_loading = status;
        },
        UPDATE_SECTORS_LOADING (state, status) {
            state.sectors_loading = status;
        },
        UPDATE_NA_LIMIT_EXCEEDED_FLAG (state, flag) {
            state.na_limit_exceeded_flag = flag;
        },
        UPDATE_CATCH_QUESTIONS_FAILED_FLAG (state, flag) {
            state.catch_questions_failed_flag = flag;
        },
        UPDATE_EMPTY_DASHBOARD_FLAG (state, flag) {
            state.empty_dashboard_flag = flag;
        },
        UPDATE_SHOW_NEXT_BUTTON_FLAG (state, flag) {
            state.show_next_button = flag;
        },
    }
});