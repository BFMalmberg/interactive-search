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
          The average price for your search is around €{{ Math.ceil(median_price) }}.
          Would you like to go lower or higher?
        </v-col>
      </v-row>
      <v-row align="center" class="justify-space-around">
        <v-col :cols="6">
          <v-btn color="secondary"
                 @click="price_selected('lower')"
          > Go lower
          </v-btn>
        </v-col>
        <v-col :cols="6">
          <v-btn color="secondary"
                 @click="price_selected('higher')"
          > Go higher
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
    ...mapState([]),
  },
  data() {
    return {
      price_range: '',
    }
  },
  methods: {
    price_selected(value) {
      const formData = {
        'user_query': this.state.query_string,
        'price': this.state.median_price,
        'button': value
      }
      if (this.query_string !== '') {
        // make an API query
        this.$http
            .post('http://localhost:5050/price_clicked', formData, {emulateJSON: true})
            .then((response) => {
              if (response.data.status === 'OK') {
                console.log(response.data);
                this.query_results = response.data.products;
                this.$emit('error_received', false)
                this.showResults = true;
                this.$emit('update_results', this.query_results);
              } else {
                this.$emit('error_received', true)
                this.showResults = false;
              }
            })
            .catch(function (error) {
              console.log(error);
              this.$emit('error_received', true)
            });
      } else {
        this.$refs.searchOperations.$refs.searchForm.validate();
        this.showResults = false;
      }
    }
  },
}
</script>

<style scoped>

</style>