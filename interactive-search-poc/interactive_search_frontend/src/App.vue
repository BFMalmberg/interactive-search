<template>
  <v-app>
    <v-overlay :opacity="0.5" :value="this.error_flag">
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
      <div v-if="showResults && !this.error_flag">
        <ProductResults
            :query_string="query_string"
            :query_results="this.query_results"
            :brands="brands"
            :error_flag="error_flag"
            @error_received="error_flag = true">
        </ProductResults>
      </div>
    </v-main>
  </v-app>
</template>

<script>
import SearchBar from './components/SearchBar';
import ProductResults from "@/components/ProductResults";

export default {
  name: 'App',

  components: {
    ProductResults,
    SearchBar,
  },

  data: () => ({
    showResults: false,
    query_string: '',
    query_results: [],
    error_flag: false,
    brands: []
  }),

  methods: {
    onClickSearch(value) {
      this.query_string = value;
      const formData = {
        'user_query': this.query_string
      }

      if (this.query_string !== '') {
        // make an API query
        this.$http
            .post('http://localhost:5050/query_results', formData, {emulateJSON: true})
            .then((response) => {
              if (response.data.status === 'OK') {
                console.log(response.data);
                this.query_results = response.data.products;
                this.brands = response.data.brands;
                this.setErrorFlag(false);
                this.showResults = true;
              } else {
                this.setErrorFlag(true);
                this.showResults = false;
              }
            })
            .catch(function (error) {
              console.log(error);
              this.setErrorFlag(true);
            });
      } else {
        this.$refs.searchOperations.$refs.searchForm.validate();
        this.showResults = false;
      }
    },
    onClearSearch() {
      this.showResults = false;
      this.$refs.searchOperations.$refs.searchForm.resetValidation();
      this.setErrorFlag(false);
      this.query_string = '';
    },
    setErrorFlag(val) {
      this.error_flag = val;
    },
    reloadPage() {
      window.location.reload();
    }
  }
};
</script>
