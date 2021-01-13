/**

 * @author srv-desarrollo
*/
         
           
                 
            Ext.onReady(function(){
            	
            	// para que la funcion ajax sea recibida se utiliza el Ext.require siguiente: 
            	
            	Ext.require(["Ext.util.Cookies", "Ext.Ajax"], function(){
                       // Add csrf token to every ajax request
                     var token = Ext.util.Cookies.get('csrftoken');
                     if(!token){
                             Ext.Error.raise("Missing csrftoken cookie");
                     } else {
                          Ext.Ajax.defaultHeaders = Ext.apply(Ext.Ajax.defaultHeaders || {}, {
                          'X-CSRFToken': token
                         });
                      }
                });


                Ext.apply(Ext.form.VTypes, {
                    mailUnico : function(val, field) {
                        
                        var cosa = true;
                        var useremail = Ext.getCmp('email').getValue();
                        var password = Ext.getCmp('password').getValue();
               
                      
                        
                        Ext.Ajax.request({
                        	
                            url: '/univalle-music/registro/',
                            params: {
                                accion : 'validarUsuario',
                                email : useremail                                                                
                            },
                            success: function(o) {
                                if (o.responseText != 0) {
                                    field.markInvalid('Email ya existente en nuestra Base de Datos')
                                } else {
                                    field.markValid
                                    cosa = true
                                    return true
                                }
                            }
                        });

                        var email = /^(\w+)([\-+.][\w]+)*@(\w[\-\w]*\.){1,5}([A-Za-z]){2,6}$/;
                        var algo = email.test(useremail)

                        if(cosa && algo){
                            return true
                        } else {
                            field.markInvalid('Este campo de ser estar en formato Email: usuario@ejemplo.com')
                            return false
                        }
                    },
                    passwordsIguales : function(val,field){
                        var password = Ext.getCmp('password').getValue();
                        var cpassword = Ext.getCmp('password').getValue();

                        if(password == cpassword){
                            return true
                        }else{
                            field.markInvalid('Las claves deben ser iguales')
                            return false
                        }
                    
                    }
                });
              
                var formRegister = Ext.create('Ext.form.Panel', {
                    frame: false, 
                    border: false,
                    buttonAlign: 'center',
                    url: '/univalle-music/registro/',
                    id: 'frmRegister',
                    bodyStyle: 'padding:10px 10px 15px 15px;background:#dfe8f6;',
                    width: 300,
                    labelWidth: 200,
                    baseParams: {
                        accion : 'registrarUsuario'
                    },
                    standardSubmit: true,
                    items: [{
                            xtype: 'textfield',
                            fieldLabel: 'Nombres',
                            name: 'nombres',
                            //id: 'regUsername',
                            allowBlank: false
                            //vtype: 'uniqueusername'
                        },{
                            xtype: 'textfield',
                            fieldLabel: 'Apellidos',
                            name: 'apellidos',
                            //id: 'regUsername',
                            allowBlank: false
                        },{
                            xtype: 'textfield',
                            fieldLabel: 'Email',
                            id: 'email',
                            name: 'email',
                            //vtype:'email',
                            allowBlank: false,
                            vtype: 'mailUnico'
                        },{
                            xtype: 'textfield',
                            fieldLabel: 'Clave',
                            name: 'password',
                            id: 'password',
                            allowBlank: false,
                            inputType: 'password'
                        }, {
                            xtype: 'textfield',
                            fieldLabel: 'Confirmar clave',
                            name: 'cpassword',
                            id: 'cpassword',
                            allowBlank: false,
                            inputType: 'password'
                            //vtype: 'passwordsIguales'
                        }, {
                            xtype: 'textfield',
                            fieldLabel: 'Numero Celular',
                            name: 'celular',
                            //id: 'regUsername',
                            allowBlank: false
                        },{
                            xtype: 'textfield',
                            fieldLabel: 'Operador Celular',
                            name: 'operador',
                            //id: 'regUsername',
                            allowBlank: false
                        }
                    ],
                    buttons: [{
                            text: 'Registrar',
                            formBind: true,
                            //disabled: true,
                            handler: function() {
                                var form = this.up('form').getForm();
                                if (form.isValid()) {
                                    form.submit({
                                        success: function(form, action) {                                            
                                            Ext.Msg.alert('Exitoso','It worked');
                                        },
                                        failure: function(form, action) {
                                            var mensaje = eval(action.result);
                                            Ext.Msg.alert('Fallo', mensaje.mensaje);
                                        }
                                    });
                                }else{
                                    Ext.Msg.alert('Error', 'Por favor comuniquese con el administrador del sistema')
                                }
                            }
                        },{
                            text: 'Borrar Campos',
                            handler: function() {
                                formRegister.getForm().reset();
                            }
                        }]
                });

                var winRegister = new Ext.Window({
                    title: 'Registro de usuarios en Univalle-Music',
                    layout: 'fit',
                    width: 350,
                    height: 350,
                    resizable: false,
                    closable: false,
                    items: [formRegister]
                });

                winRegister.show();
            });