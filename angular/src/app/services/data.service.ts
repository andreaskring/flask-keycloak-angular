import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) { }

  getData(): Observable<Object> {
    return this.http.get("http://localhost:5000/public")
      .pipe(
        tap(_ => console.log(_))
      );
    
      // return [{abc: "lajddlaksd"}];
  }
}
