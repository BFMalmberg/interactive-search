<template>
  <v-app>
    <v-overlay :opacity="0.5" :value="this.backend_error_flag">
      <v-card class="mx-auto" dark width="500">
        <v-card-title class="headline">
          Nothing useful found!
        </v-card-title>
        <v-divider color="#F7C730"></v-divider>
        <v-card-text class="text-wrap">
          Oops... The query you have entered did not match any products.
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="#F7C730"
              light
              text
              @click="reloadPage"
          >
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-overlay>

    <v-app-bar
        app
        color="#1F22A9"
        dark
    >
      <div class="d-flex align-center">
        <v-img
            :src="require('./assets/logo.png')"
            alt="VQD Logo"
            class="shrink mr-2"
            contain
            transition="scale-transition"
            width="40"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn
          href="https://www.viqtordavis.com/nl-nl/"
          target="_blank"
          text
      >
        <span class="mr-2">Official Website</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <SearchBar ref="searchOperations" @cleared="onClearSearch" @clicked="onClickSearch"></SearchBar>
      <div v-if="this.show_results_flag && !this.backend_error_flag">
        <ProductResults>
        </ProductResults>
      </div>
    </v-main>
  </v-app>
</template>

<script>
import SearchBar from './components/SearchBar';
import ProductResults from "@/components/ProductResults";
import {mapState} from "vuex";

export default {
  name: 'App',
  computed: {
    ...mapState([
      'query_string',
      'query_results',
      'brands',
      'median_price',
      'show_results_flag',
      'backend_error_flag',
      'results_loading_flag',
    ]),
  },
  components: {
    ProductResults,
    SearchBar,
  },
  methods: {
    async onClickSearch(value) {
      console.log(value)
      const form_data = {
        'user_query': value
      }
      await this.$store.dispatch('setQueryString', {query_string: value});
      if (this.query_string !== '') {
        await this.$store.dispatch('initResults', {form_data: form_data});
        await this.$store.dispatch('setShowResultFlag', {flag: true});
      } else {
        this.$refs.searchOperations.$refs.searchForm.validate();
        await this.$store.dispatch('setShowResultFlag', {flag: false});
      }
    },
    async onClearSearch() {
      this.$refs.searchOperations.$refs.searchForm.resetValidation();
      await this.$store.dispatch('setShowResultFlag', {flag: false});
      await this.$store.dispatch('setBackendErrorFlag', {flag: false})
      await this.$store.dispatch('setQueryString', {query_string: ''});
    },
    reloadPage() {
      window.location.reload();
    }
  }
};
</script>
