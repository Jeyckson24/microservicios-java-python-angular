package com.BackendSeguridad.ms_seguridad.Repositorios;

import com.BackendSeguridad.ms_seguridad.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioUsuario extends MongoRepository <Usuario,String> {


}
