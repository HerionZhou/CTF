module.exports = {
    name: 'getter',
    data() {
        return {
            loading: false,
            input: 'baidu.com',
            output: '',

        }
    },
    template: `           
<v-container fluid class="ma-2">   
    <ext-loading absolute :show="loading"></ext-loading>
    <v-row height="30" >    
        <v-toolbar flat >
            <v-text-field type="text" v-model="input" outline :label="$t('message.domain_or_ip_address')">       
            </v-text-field>
            <v-spacer></v-spacer>
            <v-btn elevation="2" @click="get" text class="mx-3" >{{$t("message.get")}}</v-btn>
        </v-toolbar>
    </v-row>
    <v-row>
        <v-col>
            <ext-editor v-model="output" readonly>
            </ext-editor>
        </v-col>
    </v-row> 
</v-container>          
`,
    i18n: require('./i18n'),
    methods: {
        async get() {
            this.output = '';

            if (this.input) {

                this.loading = true;

                const result = await this.$extInvoke('ext.app.provider.whois.get', this.input, this.options);

                if (result && result.success) {
                    this.output = result.output;
                } else {
                    this.output = '';
                    if (result && result.result.message) {
                        this.$store.dispatch("showSnackbar", result.message);
                    }
                }

                this.loading = false;
            }

        }
    }
}