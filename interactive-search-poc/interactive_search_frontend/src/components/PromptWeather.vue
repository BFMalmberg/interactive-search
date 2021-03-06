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
          Great choice!
          Just so you know, it is only {{ Math.ceil(this.temperature) }} degrees Celcius outside.
          Do you want to find a jacket that matches your new item?
        </v-col>
      </v-row>
      <v-row align="center" class="justify-space-around">
        <v-col :cols="6">
          <v-btn block outlined color="secondary"
                 @click="recommendation_chosen('yes')"
          > Yes
          </v-btn>
        </v-col>
        <v-col :cols="6">
          <v-btn block outlined color="secondary"
                 @click="recommendation_chosen('no')"
          > No
          </v-btn>
        </v-col>
      </v-row>
    </v-alert>
  </div>
</template>

<script>
import {mapState} from "vuex";

export default {
  name: "PromptWeather",
  computed: {
    ...mapState([
      'query_string',
      'median_price',
      'brand_choice',
      'temperature'
    ]),
  },
  data() {
    return {}
  },
  methods: {
    async recommendation_chosen(value) {

      if (value === 'yes') {
        if (this.query_string !== '') {
          await this.$store.dispatch('recommendProduct');
          await this.$store.dispatch('setShowResultFlag', {flag: true});
        } else {
          this.$refs.searchOperations.$refs.searchForm.validate();
          await this.$store.dispatch('setShowResultFlag', {flag: false});
        }
      }
      this.$emit('finished');
    }
  },
}
</script>

<style scoped>

</style>


Yes no