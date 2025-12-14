using UnityEngine;

public class BallMovement : MonoBehaviour
{
    public UDPReceive udpReceive;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
        string data = udpReceive.data;
        data = data.Remove(0, 1);
        data = data.Remove(data.Length - 1, 1);

        string[] info = data.Split(',');

        float x = 5 - float.Parse(info[0])/100;
        float y = float.Parse(info[1])/100;
        float z = -10 + float.Parse(info[2])/1000;

        gameObject.transform.localPosition = new Vector3(x, y, z);
    }
}
