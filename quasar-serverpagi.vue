<template>
  <div class="q-pa-md">
    <q-table
      title="Treats"
      :data="customers"
      :columns="columns"
      row-key="id"
      :pagination.sync="serverPagination"
      :loading="loading"
      :filter="filter"
      @request="request"

    >
      <template v-slot:top-right>
        <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </template>

    </q-table>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {

      filter: '',
      loading: false,
      serverPagination: {
        sortBy: 'desc',
        descending: false,
        page: 1,
        rowsPerPage: 15,
        rowsNumber: 745},
      columns: [
        {
          name: 'desc',
          required: true,
          label: 'Customer',
          align: 'left',
          field: row => row.id,
          format: val => `${val}`,
          sortable: true
        },
        { name: 'first_name', align: 'center', label: 'first name', field: 'first_name'},
        { name: 'fat', label: 'Fat (g)', field: 'fat' },
        { name: 'carbs', label: 'Carbs (g)', field: 'carbs' }
      ],
      customers: [],


    }
    
  },
  methods: {
    request ({ pagination, filter }) {
      // we set QTable to "loading" state
      this.loading = true

      // we do the server data fetch, based on pagination and filter received
      // (using Axios here, but can be anything; parameters vary based on backend implementation)

      axios
      .get(`http://127.0.0.1:8000/customers/?search=${this.filter}&page=${pagination.page}`)
      .then(({ data }) => {
        console.log(data)
        // updating pagination to reflect in the UI
        this.serverPagination = pagination

        // we also set (or update) rowsNumber
        this.serverPagination.rowsNumber = data.pagination.rowsNumber

        // then we update the rows with the fetched ones
        this.customers = data.data

        // finally we tell QTable to exit the "loading" state
        this.loading = false
      })
      .catch(error => {
        // there's an error... do SOMETHING

        // we tell QTable to exit the "loading" state
        this.loading = false
      })
    }
  },
  mounted () {
    // once mounted, we need to trigger the initial server data fetch
    this.request({
      pagination: this.serverPagination,
      filter: this.filter,
    })
  }
}
</script>
