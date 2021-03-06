<template>
  <div>
    <v-alert
        color="#515151"
        outlined
        dense
        text
        elevation="4"
    >
      <v-row align="center">
        <v-col class="grow">
          In this price range, the following brands stand out. Which brand has your preference?
        </v-col>
      </v-row>
      <v-row align="center" class="justify-space-around">
        <v-col v-for="brand in this.brands"
               :key="brand"
               :cols="2">
          <v-btn color="secondary"
                 @click="brand_selected(brand)"
          >{{ brand }}
          </v-btn>
        </v-col>
      </v-row>
    </v-alert>
  </div>
</template>

<script>
import {mapState} from "vuex";

export default {
  name: "Prompt",
  computed: {
    ...mapState([
      'query_string',
      'median_price',
      'price_choice',
    ]),
  },
  data() {
    return {
    }
  },
  methods: {
    async brand_selected(value) {

      let location_data = await fetch('https://ipapi.co/json/')
          .then(function (response) {
            return response.json();
          });

      const form_data = {
        'user_query': this.query_string,
        'median_price': this.median_price,
        'price_choice': this.price_choice,
        'brand_choice': value,
        'latitude': location_data.latitude,
        'longitude': location_data.longitude,
      }

      if (this.query_string !== '') {
        await this.$store.dispatch('filterResultsOnPriceAndBrand', {form_data: form_data});
        await this.$store.dispatch('setShowResultFlag', {flag: true});
      } else {
        this.$refs.searchOperations.$refs.searchForm.validate();
        await this.$store.dispatch('setShowResultFlag', {flag: false});
      }
    }
  },
}
</script>

<style scoped>

</style>