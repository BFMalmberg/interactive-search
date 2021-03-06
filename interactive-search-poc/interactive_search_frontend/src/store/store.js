import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        query_string: '',
        query_results: [],
        brands: [],
        median_price: 0,
        price_choice: '',
        brand_choice: '',
        temperature: '',
        show_results_flag: false,
        backend_error_flag: false,
        results_loading_flag: false,
    },
    actions: {
        async initResults ({commit}, {form_data}) {
            commit('UPDATE_RESULTS_LOADING_FLAG', true);
            // make an API query
            await Vue.http
                .post('http://localhost:5050/initial_query_results', form_data, {emulateJSON: true})
                .then((response) => {
                    if (response.data.status === 'OK') {
                        console.log(response.data);
                        commit('SET_QUERY_RESULTS', response.data.products);
                        commit('SET_MEDIAN_PRICE', response.data.median_price);
                        commit('UPDATE_BACKEND_ERROR_FLAG', false);
                    } else {
                        commit('UPDATE_BACKEND_ERROR_FLAG', true);
                        commit('UPDATE_SHOW_RESULTS_FLAG', false);
                    }
                })
                .catch(error => {
                    console.error(error);
                    commit('UPDATE_BACKEND_ERROR_FLAG', true);
                });

            commit('UPDATE_RESULTS_LOADING_FLAG', false);
        },
        async filterResultsOnPrice ({commit}, {form_data}) {
            commit('UPDATE_RESULTS_LOADING_FLAG', true);
            // make an API query
            await Vue.http
                .post('http://localhost:5050/price_filtered_results', form_data, {emulateJSON: true})
                .then((response) => {
                    if (response.data.status === 'OK') {
                        console.log(response.data);
                        commit('SET_QUERY_RESULTS', response.data.products);
                        commit('SET_BRANDS', response.data.brands);
                        commit('SET_PRICE_CHOICE', form_data.price_choice);
                        commit('UPDATE_BACKEND_ERROR_FLAG', false);
                    } else {
                        commit('UPDATE_BACKEND_ERROR_FLAG', true);
                        commit('UPDATE_SHOW_RESULTS_FLAG', false);
                    }
                })
                .catch(error => {
                    console.error(error);
                    commit('UPDATE_BACKEND_ERROR_FLAG', true);
                });

            commit('UPDATE_RESULTS_LOADING_FLAG', false);
        },
        async filterResultsOnPriceAndBrand ({commit}, {form_data}) {
            commit('UPDATE_RESULTS_LOADING_FLAG', true);
            // make an API query
            await Vue.http
                .post('http://localhost:5050/brand_filtered_results', form_data, {emulateJSON: true})
                .then((response) => {
                    if (response.data.status === 'OK') {
                        console.log(response.data);
                        commit('SET_QUERY_RESULTS', response.data.products);
                        commit('SET_TEMPERATURE', response.data.temperature);
                        commit('SET_BRAND_CHOICE', form_data.brand_choice);
                        commit('UPDATE_BACKEND_ERROR_FLAG', false);
                    } else {
                        commit('UPDATE_BACKEND_ERROR_FLAG', true);
                        commit('UPDATE_SHOW_RESULTS_FLAG', false);
                    }
                })
                .catch(error => {
                    console.error(error);
                    commit('UPDATE_BACKEND_ERROR_FLAG', true);
                });

            commit('UPDATE_RESULTS_LOADING_FLAG', false);
        },
        setQueryString ({commit}, {query_string}) {
            commit('SET_QUERY_STRING', query_string);
        },
        setBackendErrorFlag ({commit}, {flag}) {
            commit('UPDATE_BACKEND_ERROR_FLAG', flag);
        },
        setShowResultFlag ({commit}, {flag}) {
            commit('UPDATE_SHOW_RESULTS_FLAG', flag);
        },

    },
    mutations: {
        SET_QUERY_STRING (state, query_string) {
            state.query_string = query_string;
        },
        SET_QUERY_RESULTS (state, query_results) {
            state.query_results = query_results;
        },
        SET_BRANDS (state, brands) {
            state.brands = brands;
        },
        SET_MEDIAN_PRICE (state, median_price) {
            state.median_price = median_price;
        },
        SET_PRICE_CHOICE (state, price_choice) {
            state.price_choice = price_choice;
        },
        SET_TEMPERATURE (state, temperature) {
            state.temperature = temperature;
        },
        UPDATE_SHOW_RESULTS_FLAG (state, flag) {
            state.show_results_flag = flag;
        },
        UPDATE_BACKEND_ERROR_FLAG (state, flag) {
            state.backend_error_flag = flag;
        },
        UPDATE_RESULTS_LOADING_FLAG (state, flag) {
            state.results_loading_flag = flag;
        },

    }
});