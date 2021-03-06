<template>
  <div>
    <v-alert
        color="#515151"
        dense
        elevation="4"
        outlined
        text
    >
      <v-row align="center">
        <v-col class="grow">
          Let’s get you the item you are looking for!
          Most items in your selection are priced around €{{ Math.ceil(median_price) }}.
          Do you want to look for an item below or above this price?
        </v-col>
      </v-row>
      <v-row align="center" class="justify-space-around">
        <v-col :cols="6">
          <v-btn color="secondary"
                 @click="price_selected('lower')"
          > Below €{{ Math.ceil(median_price) }}
          </v-btn>
        </v-col>
        <v-col :cols="6">
          <v-btn color="secondary"
                 @click="price_selected('higher')"
          > Above €{{ Math.ceil(median_price) }}
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
    ]),
  },
  data() {
    return {}
  },
  methods: {
    async price_selected(value) {
      const form_data = {
        'user_query': this.query_string,
        'median_price': this.median_price,
        'price_choice': value
      }

      if (this.query_string !== '') {
        await this.$store.dispatch('filterResultsOnPrice', {form_data: form_data});
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