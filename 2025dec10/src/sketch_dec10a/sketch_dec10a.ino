#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("MPU6050 rebooting...");

  Wire.begin(21, 22);
  Wire.setClock(400000);

  mpu.initialize();

  if (!mpu.testConnection()) {
    Serial.println("❌ MPU6050 connect failed");
    while (1) delay(1000);
  }

  Serial.println("✅ MPU6050 connected!");
  delay(1000);
}

void loop() {
  int16_t ax, ay, az;
  int16_t gx, gy, gz;

  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

  Serial.print(ax);
  Serial.print(",");
  Serial.println(ay);
  Serial.print(",");
  Serial.println(az);

  delay(50);  // 20Hz
}