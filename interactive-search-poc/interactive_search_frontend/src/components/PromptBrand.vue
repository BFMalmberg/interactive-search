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
    ...mapState([]),
  },
  data() {
    return {
    }
  },
  methods: {
    brand_selected(value) {
      const formData = {
        'user_query': this.$store.state.query_string,
        'brand_name': value
      }
      if (this.query_string !== '') {
        // make an API query
        this.$http
            .post('http://localhost:5050/query_brand', formData, {emulateJSON: true})
            .then((response) => {
              if (response.data.status === 'OK') {
                console.log(response.data);
                this.query_results = response.data.products;
                this.$emit('error_received', false)
                this.showResults = true;
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