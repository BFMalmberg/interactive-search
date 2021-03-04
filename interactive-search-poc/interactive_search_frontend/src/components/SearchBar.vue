<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
            :src="require('../assets/viqtordavis.png')"
            class="my-3"
            contain
            height="80"
        />
      </v-col>

      <v-col class="mb-2">
        <h3 class="display-1 font-weight-bold mb-3">
          Welcome to Interactive Product Search Tool
        </h3>
        <p>Type your query and hit enter to explore our product range.</p>
      </v-col>

      <v-col cols="12">
        <v-form
            ref="searchForm"
            v-model="valid"
            v-on:submit.prevent="onSubmit">
          <v-text-field
              v-model="user_query"
              :rules="queryRules"
              append-icon="mdi-magnify"
              clearable
              filled
              label="What are you looking for?"
              required
              solo
              @click:clear="onClear"
          >
          </v-text-field>
        </v-form>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>

export default {
  name: 'SearchBar',
  data: () => ({
    valid: false,
    user_query: '',
    queryRules: [
      v => !!v || 'Query is required',
    ],
  }),
  methods: {
    async onSubmit() {
      this.showMap = true;
      this.$emit('clicked', this.user_query);
    },
    onClear: function () {
      this.user_query = '';
      this.$emit('cleared');
      this.$refs.searchForm.resetValidation();
    },
  }
}
</script>
